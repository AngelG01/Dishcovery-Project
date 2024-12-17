from django.views.generic import ListView

from dishcovery_project.recipes.models import Recipe


# Create your views here.
class HomePageView(ListView):
    model = Recipe
    template_name = 'common/home-page.html'
    context_object_name = 'recipes'
    paginate_by = 10
    ordering = ['-created_at']
