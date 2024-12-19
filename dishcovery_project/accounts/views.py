from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView

from dishcovery_project.accounts.forms import CustomUserCreationForm, CustomUserAuthenticationForm, ProfileEditForm
from dishcovery_project.accounts.models import Profile

UserModel = get_user_model()


# Create your views here
class RegisterUserView(CreateView):
    model = UserModel
    form_class = CustomUserCreationForm
    template_name = 'account/registration_page.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()

        profile, _ = Profile.objects.get_or_create(user=user)
        profile.username = user.username
        profile.save()

        return super().form_valid(form)


class LoginUserView(LoginView):
    template_name = 'account/login_page.html'
    form_class = CustomUserAuthenticationForm

    def form_valid(self, form):
        super().form_valid(form)
        profile_instance, _ = Profile.objects.get_or_create(user=self.request.user)
        return HttpResponseRedirect(self.get_success_url())


class LogoutUserView(LogoutView):
    pass


class ProfileDetailsView(LoginRequiredMixin, DetailView):
    model = Profile
    template_name = 'account/profile-details.html'
    context_object_name = 'profile'

    def get_object(self, queryset=None):
        profile, _ = Profile.objects.get_or_create(user=self.request.user)
        return profile


class ProfileEditView(UpdateView):
    model = UserModel
    form_class = ProfileEditForm
    template_name = 'account/edit_profile.html'

    def get_object(self, queryset=None):
        # Returns the profile instance to be edited
        return self.request.user.profile

    def form_valid(self, form):
        # Save the Profile form first
        profile = form.save(commit=False)
        profile.save()

        # Sync the username with the UserModel (custom user model)
        user = self.request.user
        if user.username != profile.username:
            user.username = profile.username
            user.save()

        # Return a redirect to the success URL
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        # Return the URL to the profile details page
        return reverse_lazy('profile-details', kwargs={'pk': self.request.user.profile.pk})
