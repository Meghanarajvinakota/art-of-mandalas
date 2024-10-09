from django.contrib import admin
from .models import About
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.

@admin.register(About)
class AboutAdmin(SummernoteModelAdmin):
    """
    Adds text editing of the body in admin panel
    """

    summernote_fields = ('content',)
    