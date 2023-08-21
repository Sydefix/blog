from django.contrib import admin
from .models import Comment

class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'post', 'created_at')
    list_filter = ('author', 'post', 'created_at')
    search_fields = ('author__username', 'post__title')

admin.site.register(Comment, CommentAdmin)
