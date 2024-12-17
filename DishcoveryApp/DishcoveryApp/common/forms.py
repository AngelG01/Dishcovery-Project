from django import forms
from django.contrib.auth import get_user_model

from DishcoveryApp.common.models import Ratings, Comments

UserModel = get_user_model()


class RatingForm(forms.Form):
    score = forms.ChoiceField(
        choices=[(i, f'{i} Star{"s" if i > 1 else ""}') for i in range(1, 6)],
        widget=forms.RadioSelect,
        required=True,
    )


class CommentForm(forms.Form):
    content = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'Write your comment here...'}),
        required=True,
    )
