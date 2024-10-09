from django.contrib import admin
from .models import Share
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.


@admin.register(Share)
class ShareAdmin(admin.ModelAdmin):
    """
    Lists fields for display in name ,title and approved
    """
    list_display = ('name', 'title', 'approved')
    list_filter = ('approved',)  # Add filter by approval status
    actions = ['approve_shares']

    def approve_shares(self, request, queryset):
        queryset.update(approved=True)
        self.message_user(request, "Selected shares have been approved.")

    approve_shares.short_description = "Approve selected shares"
