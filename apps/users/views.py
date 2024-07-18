from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.db import IntegrityError
from django.contrib.auth.views import LogoutView
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from apps.users.forms import CustomUserRegisterForm, EditProfileForm

from apps.users.forms import CustomAuthenticationForm
from apps.users.forms import CustomUserRegisterForm


class CustomLogoutView(LogoutView):
    def dispatch(self, request, *args, **kwargs):
        logout(request)
        messages.success(request, 'You have successfully logged out.')
        return redirect('/')

class CustomLoginView(LoginView):
    template_name = 'user/log_in.html'
    authentication_form = CustomAuthenticationForm

    def form_valid(self, form):
        login(self.request, form.get_user())
        messages.success(self.request, 'You have successfully logged in.')
        return redirect('/')

def register(request):
    if request.method == 'POST':
        form = CustomUserRegisterForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                user = form.save()
                login(request, user)
                messages.success(request, 'Registration successful.')
                return redirect('index')
            except IntegrityError:
                form.add_error('username', 'Username is already taken.')
        else:
            messages.error(request, 'Registration failed. Please correct the errors below.')
    else:
        form = CustomUserRegisterForm()

    context = {
        'form': form
    }
    return render(request, 'user/register.html', context)

@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully.')
            return redirect('profile')
    else:
        form = EditProfileForm(instance=request.user)

    context = {
        'form': form
    }
    return render(request, 'user/edit_profile.html', context)

@login_required
def delete_profile(request):
    if request.method == 'POST':
        user = request.user
        user.delete()
        messages.success(request, 'Your profile was successfully deleted!')
        return redirect('/')
    return render(request, 'user/delete_profile.html')

@login_required
def profile(request):
    return render(request, 'user/profile.html', {'user': request.user})

