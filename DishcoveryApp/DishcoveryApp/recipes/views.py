from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Avg
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView

from DishcoveryApp.common.forms import RatingForm, CommentForm
from DishcoveryApp.common.models import Ratings, Comments
from DishcoveryApp.recipes.forms import CreateRecipeForm
from DishcoveryApp.recipes.models import Recipe


# Create your views here.
class AddRecipeView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Recipe
    form_class = CreateRecipeForm
    template_name = 'recipes/add-recipe-page.html'
    success_url = reverse_lazy('home-page')
    success_message = 'Your recipe has been successfully added!'

    def form_valid(self, form):
        recipe = form.save(commit=False)
        recipe.author = self.request.user

        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class RecipeDetailsView(DetailView):
    model = Recipe
    template_name = 'recipes/recipe-details-page.html'
    context_object_name = 'recipe'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Get the average rating for the recipe
        average_rating = Ratings.objects.filter(recipe=self.object).aggregate(Avg('score'))['score__avg']
        context['average_rating'] = round(average_rating, 1) if average_rating else 0

        # Get all the comments for the recipe
        context['comments'] = Comments.objects.filter(recipe=self.object)

        # Add the forms for rating and comment submission
        context['rating_form'] = RatingForm()
        context['comment_form'] = CommentForm()

        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        recipe = self.object

        if 'rating' in request.POST:
            # Handle rating submission
            rating_form = RatingForm(request.POST)
            if rating_form.is_valid():
                score = rating_form.cleaned_data['score']
                Ratings.objects.update_or_create(
                    recipe=recipe,
                    user=request.user,
                    defaults={'score': score}
                )
                return redirect(reverse('recipe-details', kwargs={'pk': recipe.id}))

        elif 'comment' in request.POST:
            # Handle comment submission
            comment_form = CommentForm(request.POST)
            if comment_form.is_valid():
                comment = comment_form.cleaned_data['content']
                Comments.objects.create(
                    recipe=recipe,
                    user=request.user,
                    content=comment
                )
                return redirect(reverse('recipe-details', kwargs={'pk': recipe.id}))

        return self.get(request, *args, **kwargs)
