from django.contrib import admin
from django.contrib import admin
from stock.models import Persona,Vestimenta

# Register your models here.

class PersonaAdmin(admin.ModelAdmin):
    list_display=("nombre","apellido","dni","celular","mail")
    search_fields=("nombre","apellido","dni","celular","mail")


class VestimentaAdmin(admin.ModelAdmin):
    list_display=("ropa","zapatos","pulsera")
    list_display=("ropa","zapatos","pulsera")


admin.site.register(Persona,PersonaAdmin)
admin.site.register(Vestimenta,VestimentaAdmin)

admin.site.site_header = "Sitio web de Stock"
admin.site.site_title = "Portal de Stock"
admin.site.index_title = "Bienvenidos Web de Administración"

# Register your models here.
