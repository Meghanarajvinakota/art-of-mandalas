from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    """
    Lists fields for display in admin, search & filter fields.
    """

    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'content']
    list_filter = ('status', 'created_on',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """
    Lists fields for display in admin, search & filter fields.
    """

    list_display = ('author', 'body', 'approved')
    list_filter = ('approved',)  # Add filter by approval status
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)
        self.message_user(request, "Selected comments have been approved.")  # Confirmation message

    approve_comments.short_description = "Approve selected comments"  # Description for the action

# Register your models here.


