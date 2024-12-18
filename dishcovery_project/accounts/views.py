from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView

from dishcovery_project.accounts.forms import CustomUserCreationForm, CustomUserAuthenticationForm, ProfileEditForm
from dishcovery_project.accounts.models import Profile

UserModel = get_user_model()


# Create your views here
class RegisterUserView(CreateView):
    model = UserModel
    form_class = CustomUserCreationForm
    template_name = 'account/registration_page.html'
    success_url = reverse_lazy('login')


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
        return self.request.user.profile

    def get_success_url(self):
        # Using the profile pk explicitly instead of self.object.pk
        return reverse_lazy('profile-details', kwargs={'pk': self.request.user.profile.pk})


class ProfileDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Profile
    template_name = 'account/profile_delete_page.html'
    success_url = reverse_lazy('login')

    def test_func(self):
        profile = self.get_object_or_404(Profile, pk=self.kwargs['pk'])
        return self.request.user == profile
