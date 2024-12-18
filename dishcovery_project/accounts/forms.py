from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm

from dishcovery_project.accounts.models import Profile

UserModel = get_user_model()


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = UserModel
        fields = ('email', 'username')


class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = UserModel


class CustomUserAuthenticationForm(AuthenticationForm):
    username = forms.EmailField(widget=forms.TextInput(attrs={'autofocus': 'True'}))
    password = forms.CharField(
        label='Password',
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password'}),
    )


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('username', 'date_of_birth', 'profile_picture')
        labels = {
            'username': 'Username',
            'date_of_birth': 'Date of Birth',
            'profile_picture': 'Profile Picture',
        }
