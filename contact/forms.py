from .models import ContactForm
from django import forms


class ContactUsForm(forms.ModelForm):
    """
    Form to allow to give details of user that are name ,emial and messgaeon the contact form
    """
    class Meta:
        model = ContactForm
        fields = ('name', 'email', 'message')
