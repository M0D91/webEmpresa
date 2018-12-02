from django.contrib import admin
from .models import Link

# Register your models here.
class LinkAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')

    def get_readonly_fields(self, request, obj=None):
        if request.user.groups.filter(name='Personal').exists():
            return ('key','name')
        else:
            return ('created','updated')

# Añade la entrada manual que hemos creado para el admin de Django
admin.site.register(Link, LinkAdmin)