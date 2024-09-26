from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    """
    Form to allow customization on the comment form
    """
    class Meta:
        model = Comment
        fields = ('body',)