from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import RegisterUserForm


class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'authentication/login.html'


def logout_view(request):
    logout(request)
    return redirect('auth:login')


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'authentication/register.html'
    success_url = reverse_lazy('auth:login')
    context_object_name = 'form'
