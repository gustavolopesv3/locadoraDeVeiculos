
from django.contrib import admin
from .models import *

class veiculoAdmin(admin.ModelAdmin):
    search_fields = ['modelo']
    list_display = ['id','modelo','ano','status']
    list_editable = ['modelo','ano','status']


admin.site.register(Cliente)
admin.site.register(Alguel)
admin.site.register(Modelo)
admin.site.register(Marcas)
admin.site.register(Veiculo, veiculoAdmin)
