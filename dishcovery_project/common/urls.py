from django.urls import path

from dishcovery_project.common.views import HomePageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home-page'),

]
