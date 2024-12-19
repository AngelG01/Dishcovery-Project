from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView

from dishcovery_project.common.forms import CommentForm
from dishcovery_project.common.models import Comment
from dishcovery_project.recipes.forms import CreateRecipeForm, EditRecipeForm
from dishcovery_project.recipes.models import Recipe


# Create your views here.
class AddRecipeView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Recipe
    form_class = CreateRecipeForm
    template_name = 'recipes/add_recipe_page.html'
    success_url = reverse_lazy('home-page')
    success_message = 'Your recipe has been successfully added!'

    def form_valid(self, form):
        recipe = form.save(commit=False)
        recipe.author = self.request.user

        return super().form_valid(form)


class RecipeDetailsView(LoginRequiredMixin, DetailView):
    model = Recipe
    template_name = 'recipes/recipe_details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = self.object.comments.all()
        context['comment_form'] = CommentForm()
        return context

    def post(self, request, *args, **kwargs):
        recipe = self.get_object()
        form = CommentForm(request.POST)

        if form.is_valid():
            Comment.objects.create(
                recipe=recipe,
                user=request.user,
                content=form.cleaned_data['content']
            )
            # Redirect to the same page to refresh comments
            return redirect('recipe-details', pk=recipe.pk)

        return self.get(request, *args, **kwargs)


class RecipeEditView(LoginRequiredMixin, UpdateView):
    model = Recipe
    form_class = EditRecipeForm
    template_name = 'recipes/recipe_edit.html'
    context_object_name = 'recipe'

    # Redirect to the recipe detail page after successful update
    def get_success_url(self):
        return reverse_lazy('recipe-details', kwargs={'pk': self.object.pk})

    # Only allow users to edit their own recipes
    def get_queryset(self):
        return Recipe.objects.filter(author=self.request.user)
