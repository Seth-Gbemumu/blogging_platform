from django.contrib import admin
from .models import Post, Category, Tag

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date')
    search_fields = ('title', 'content')
    list_filter = ('category', 'tags')

admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Tag)

