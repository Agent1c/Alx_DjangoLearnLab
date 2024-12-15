from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# Create your views here.

# register view model

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login') # Redirect to login page after registration
        else:
            form = CustomUserCreationForm()
        return render(request, 'blog/register.html', {'form' : form})
    

# simple profile view where users can see their details.
@login_required
def profile(request):
    return render(request, 'blog/profile.html', {'user' : request.user})
    


class PostListView(ListView):
    model = Post
    template_name = 'post_list.html'  # template name
    context_object_name = 'posts'  # Default is 'object_list'

class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'  # template name
    context_object_name = 'post'  # Default is 'object'

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'post_form.html'  # template name
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = 'post_form.html'  # template name
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'post_confirm_delete.html'  # template name
    success_url = reverse_lazy('post-list')

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author
    
class CommentCreateView(LoginRequiredMixin, View):
    def post(self, request, post_id):
        post = get_object_or_404(Post, id=post_id)
        form = CommentForm(request.POST)
        if form.is_valid():
            Comment = form.save(commit=False)
            Comment.post = post
            Comment.author = request.user
            Comment.save()
        
        return redirect('post-detail', pk=post_id)
    
class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, View):
    def get(self, request, post_id, comment_id):
        comment = get_object_or_404(Comment, id = comment_id)
        form = CommentForm(instance=comment)
        return render(request, 'blog/comment_update.html', {'form': form, 'comment': comment})
    
    def post(self, request, post_id, comment_id):
        comment = get_object_or_404(Comment, id=comment_id)
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('post-detail')
        
    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.author
    
class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, View):
        def post(self, request, post_id, comment_id):
            comment = get_object_or_404(Comment, request, id=comment_id)
            comment.delete()
            return redirect('post-detail', pk=post_id)

        def test_func(self):
            comment = self.get_object()
            return self.request.user == comment.author
        

def search(request):
    query = request.GET.get('q')
    posts = Post.objects.filter(
        Q(title__icontains=query) | 
        Q(content__icontains = query) | 
        Q(tags__name__icontains=query)
    ).distinct() # distinct used to avoid duplicate results from multiple tags
    return render(request, 'blog/search_results.html', {'posts': posts, 'query': query})

class TaggedPostListView(ListView):
    model = Post
    template_name = 'blog/tagged_posts.html'

    def get_queryset(self):
        tag_name = self.kwargs['tag_name']
        return Post.objects.filter(tags__name__iexact=tag_name)
    
class PostByTagListView(ListView):
    """
    ListView to display posts filtered by tag.
    """
    model = Post
    template_name = "blog/tagged_posts.html"
    context_object_name = 'posts'
    paginate_by = 5  # Optional: paginate results if too many posts exist.

    def get_queryset(self):
        """
        Fetch posts that are associated with the specific tag.
        """
        slug = self.kwargs.get('tag_slug')
        return Post.objects.filter(tags__slug=slug)