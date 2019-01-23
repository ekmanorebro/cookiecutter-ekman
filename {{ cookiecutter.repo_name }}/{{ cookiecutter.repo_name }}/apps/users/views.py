from django.shortcuts import render, redirect
from django.views.generic import DetailView, FormView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from .forms import UserCreationForm

User = get_user_model()

class RegisterFormView(FormView):
  form_class = UserCreationForm
  template_name = "registration/register.html"

class UserLoginView(LoginView):
  pass

class UserLogoutView(LoginRequiredMixin, LogoutView):
  pass

class UserDetailView(LoginRequiredMixin, DetailView):
  model = User
