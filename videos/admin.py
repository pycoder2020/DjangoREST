from django.contrib import admin
from .models import Video, Comment


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'created_at']
    search_fields = ['id', 'title']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['author', 'video', 'created_at']
    list_filter = ['video']
    search_fields = ['author', 'text']
