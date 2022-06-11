from django.contrib import admin
from .models import *

admin.site.register(EspecificacionProducto)
class EspecificacionDetalleInline(admin.TabularInline):
    model = EspecificacionProductoDetalle
    
@admin.register(Productos)
class ProductosAdmin(admin.ModelAdmin):
    inlines = [EspecificacionDetalleInline]

admin.site.register(Cliente)
admin.site.register(Region)
admin.site.register(Comuna)
admin.site.register(Provincia)