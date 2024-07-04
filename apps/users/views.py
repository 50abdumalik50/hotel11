from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.db import IntegrityError
from django.contrib.auth.views import LogoutView
from django.contrib.auth import logout


from .forms import CustomAuthenticationForm
from .forms import CustomUserRegisterForm


class CustomLogoutView(LogoutView):
    def dispatch(self, request, *args, **kwargs):
        logout(request)
        messages.success(request, 'You have successfully logged out.')
        return redirect('/')


class CustomLoginView(LoginView):
    template_name = 'user/log_in.html'
    authentication_form = CustomAuthenticationForm

    def form_valid(self, form):
        # This method is called when form is valid
        login(self.request, form.get_user())
        messages.success(self.request, 'You have successfully logged in.')
        return redirect('/')


def register(request):
    if request.method == 'POST':
        form = CustomUserRegisterForm(request.POST)
        if form.is_valid():
            try:
                user = form.save()
                login(request, user)
                messages.success(request, 'Registration successful.')
                return redirect('../../')
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

# def register(request):
#     if request.method == 'POST':
#         form = UserRegisterForm(request.POST)
#         if form.is_valid():
#             user_form = form.save()
#             login(request, user_form)
#             return redirect('/')
#     else:
#         form = UserRegisterForm()
#     return render(request, 'user/register.html', locals())
#
#
# class CreateUserView(CreateView):
#     model = User
#     form_class = UserRegisterForm
#     success_url = reverse_lazy('login')
#     template_name = 'user/register.html'



