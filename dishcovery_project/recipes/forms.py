from django import forms

from dishcovery_project.recipes.models import Recipe


class CreateRecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'description', 'ingredients', 'instructions', 'image']  # Make sure to include all fields

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Recipe Title'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Write description here...'}),
            'ingredients': forms.Textarea(
                attrs={'class': 'form-control', 'placeholder': 'Write needed ingredients here...'}),
            'instructions': forms.Textarea(
                attrs={'class': 'form-control', 'placeholder': 'Write cooking instructions here...'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'})
        }


class EditRecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['description', 'ingredients', 'instructions']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4, 'cols': 50}),
            'ingredients': forms.Textarea(attrs={'rows': 4, 'cols': 50}),
            'instructions': forms.Textarea(attrs={'rows': 6, 'cols': 50}),
        }
