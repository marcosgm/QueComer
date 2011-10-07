from dietas.models import *
from django.contrib import admin

class IngredienteAdmin(admin.ModelAdmin):

    list_display = ['nombre', 'tipo', 'grCHidratox100', 'grProteinax100', 'grGrasax100', 'kcalx100']

admin.site.register(Ingrediente,IngredienteAdmin)
admin.site.register(TipoAlimento)
admin.site.register(Plato)

