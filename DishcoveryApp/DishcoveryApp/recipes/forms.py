from django import forms

from DishcoveryApp.recipes.models import Recipe


class CreateRecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'ingredients', 'instructions', 'image']

        widgets = {
            'title':
                forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Recipe Title'}),
            'ingredients': forms.Textarea(
                attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'List ingredients here...'}),
            'instructions': forms.Textarea(
                attrs={'class': 'form-control', 'placeholder': 'Write cooking nstructions here...'}),
            'image':
                forms.ClearableFileInput(attrs={'class': 'form-control'})
        }
