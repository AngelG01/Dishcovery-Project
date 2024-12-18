from django.urls import path, include

from dishcovery_project.accounts.views import RegisterUserView, LoginUserView, LogoutUserView, ProfileDetailsView, \
    ProfileEditView, ProfileDeleteView

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register'),
    path('login/', LoginUserView.as_view(), name='login'),
    path('logout/', LogoutUserView.as_view(), name='logout'),
    path('profile/<int:pk>', include([
        path('', ProfileDetailsView.as_view(), name='profile-details'),
        path('edit_profile/', ProfileEditView.as_view(), name='edit-profile'),
        path('delete/', ProfileDeleteView.as_view(), name='delete-profile'),
    ]))
]
