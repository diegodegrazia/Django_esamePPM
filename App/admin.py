from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'created_on')
    list_filter = ('status',)
    search_fields = ['status', 'content']


admin.site.register(Post, PostAdmin)