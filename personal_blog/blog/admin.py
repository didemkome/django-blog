from django.contrib import admin

from blog.models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'update_at']
    list_display_links = ['title']
    list_filter = ['status' ]
    ordering = ['-update_at', 'title', 'id'] 
    search_fields = ['title']
