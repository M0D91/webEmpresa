from django.contrib import admin
from .models import Page

# Register your models here.
class PageAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')
    list_display = ('title','order')

# Añade la entrada manual que hemos creado para el admin de Django
admin.site.register(Page, PageAdmin)