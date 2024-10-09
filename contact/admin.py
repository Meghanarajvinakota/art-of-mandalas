from django.contrib import admin
from .models import ContactForm
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.

@admin.register(ContactForm)
class ContactFormAdmin(admin.ModelAdmin):
    """
    Lists fields for display in admin,message and read.
    """

    list_display = ('message', 'read',)
