from django.contrib import admin
from posts.models import Post, Comment, Tag


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'content', 'created_at']
    search_fields = ['title']
    list_display_links = ['id', 'title']
    list_filter = ['title']
    list_editable = ['content']


admin.register(Post, PostAdmin)
admin.site.register(Comment)
admin.site.register(Tag)
