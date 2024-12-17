from django.shortcuts import render
from django.views.generic import TemplateView

from DishcoveryApp.recipes.models import Recipe


# Create your views here.
class HomePageView(TemplateView):
    template_name = 'common/home-page.html'

    def get_context_data(self, **kwargs):
        # Get all recipes from the database
        recipes = Recipe.objects.all()

        # If no recipes are found, set a message
        if not recipes:
            empty_message = "It's so empty here! There are no recipes yet!"
        else:
            empty_message = ""

        context = {
            'recipes': recipes,
            'empty_message': empty_message,
        }
        return context
