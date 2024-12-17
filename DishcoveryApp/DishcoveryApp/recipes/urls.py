from django.urls import path, include

from DishcoveryApp.recipes.views import AddRecipeView, RecipeDetailsView

urlpatterns = [
    path('add-recipe/', AddRecipeView.as_view(), name='add-recipe'),
    path('<int:pk>/', include([
        path('', RecipeDetailsView.as_view(), name='recipe-details'),
    ])),
]
