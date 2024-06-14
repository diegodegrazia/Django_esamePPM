from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .models import Post, Comment, Blog


class BlogAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'author', 'created_on', 'updated_on')
    list_filter = ('author', 'created_on',)
    search_fields = ['name', 'slug']
    fields = ['name', 'author']


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'blog', 'created_on', 'updated_on')
    list_filter = ('status', 'created_on',)
    search_fields = ['title', 'slug', 'content']
    fields = ['title', 'author', 'blog', 'content', 'status']


class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'post', 'author', 'created_on', 'updated_on')
    list_filter = ('author', 'post', 'created_on',)
    search_fields = ['id', 'content']
    fields = ['author', 'post', 'content']


class CustomUserAdmin(UserAdmin):

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Informazioni personali', {'fields': ('first_name', 'last_name', 'email')}),
        ('Permessi', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
    )

    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    search_fields = ('username', 'first_name', 'last_name')
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'first_name', 'last_name', 'password1', 'password2'),
        }),
    )


admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Blog, BlogAdmin)
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
