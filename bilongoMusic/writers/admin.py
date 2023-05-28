from django.contrib import admin
from .models import Writer

# Register your models here.

class WriterAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'email', 'telefono')
    list_display_links = ('id', 'nombre')
    search_fields = ('nombre',)
    list_per_page = 25

admin.site.register(Writer, WriterAdmin)