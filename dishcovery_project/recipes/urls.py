from django.urls import path, include

from dishcovery_project.recipes.views import AddRecipeView, RecipeDetailsView, RecipeEditView

urlpatterns = [
    path('add_recipe/', AddRecipeView.as_view(), name='add-recipe'),
    path('<int:pk>/', include([
        path('', RecipeDetailsView.as_view(), name='recipe-details'),
        path('recipe_edit/', RecipeEditView.as_view(), name='recipe-edit'),

    ]))
]
