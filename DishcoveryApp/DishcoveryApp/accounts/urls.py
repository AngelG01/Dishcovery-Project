from django.contrib.auth.views import LogoutView
from django.urls import path

from DishcoveryApp.accounts.views import UserProfileLogin, UserProfileRegisterView

urlpatterns = [
    path('login/', UserProfileLogin.as_view(), name='login'),
    path('register/', UserProfileRegisterView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
