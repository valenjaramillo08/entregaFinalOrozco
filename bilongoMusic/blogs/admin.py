from django.contrib import admin
from .models import Blog
# Register your models here.

class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_publish', 'categoria', 'writer', 'fecha')
    list_display_links = ('id', 'title')
    list_filter = ('writer',)
    list_editable = ('is_publish',)
    search_fields = ('title', 'fecha', 'texto', 'extra')
    list_per_page = 25

admin.site.register(Blog, ListingAdmin)