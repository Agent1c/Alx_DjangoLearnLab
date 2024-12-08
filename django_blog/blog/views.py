from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required

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
    