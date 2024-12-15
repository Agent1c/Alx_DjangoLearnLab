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
    template_name = 'blogpost_list.html'  # template name
    context_object_name = 'posts'  # Default is 'object_list'

class PostDetailView(DetailView):
    model = Post
    template_name = 'blogpost_detail.html'  # template name
    context_object_name = 'post'  # Default is 'object'

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'blogpost_form.html'  # template name
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = 'blogpost_form.html'  # template name
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blogpost_confirm_delete.html'  # template name
    success_url = reverse_lazy('blogpost-list')

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author