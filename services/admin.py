from django.contrib import admin
from .models import Service

# Register your models here.
class ServiceAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')

# Añade la entrada manual que hemos creado para el admin de Django
admin.site.register(Service,ServiceAdmin)
