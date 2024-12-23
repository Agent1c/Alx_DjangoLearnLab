from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# Customer customer creation form
class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

        def save(self, commit=True):
            user = super().save(commit=False)
            user.email = self.cleaned_data['email']
            if commit:
                user.save()
            return user

class PostForm(forms.ModelForm):
    #  ModelForm for creating/updating blog posts with tagging support.

    class Meta:
        models = Post
        fields = ['title', 'content', 'tags']
        widgets = {
            'tags': TagWidget(),
        }
        
    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['title'].label = "Blog Post Title"
        self.fields['content'].label = "Blog Post Content"
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']