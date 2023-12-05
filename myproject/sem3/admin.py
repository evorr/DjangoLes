from django.contrib import admin
from .models import Author, Article, Comment


class AuthorAdmin(admin.ModelAdmin):
    """List of products"""
    list_display = ['name', 'email']
    ordering = ['name']
    list_filter = ['birthday']
    search_fields = ['biography']
    search_help_text = 'Search by biography'
    readonly_fields = ['name', 'last_name']


admin.site.register(Author, AuthorAdmin)
#admin.site.register(Article)
#admin.site.register(Comment)
