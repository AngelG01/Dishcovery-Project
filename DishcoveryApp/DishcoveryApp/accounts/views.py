from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from DishcoveryApp.accounts.forms import UserProfileCreationForm

UserModel = get_user_model()


# Create your views here.
class UserProfileLogin(LoginView):
    template_name = 'accounts/login_page.html'


class UserProfileRegisterView(CreateView):
    model = UserModel
    form_class = UserProfileCreationForm
    template_name = 'accounts/registration_page.html'
    success_url = reverse_lazy('home-page')

