from .models import Share
from django import forms



class ShareABookForm(forms.ModelForm):
    """
   Form to allow to give details of user that are title ,author and picture the share a book form
    """
    class Meta:
        model = Share
        fields = ('title', 'author', 'picture',)