from django.contrib import admin
from .models import Editorial, Autor, Producto, Bodega, MovimientoProducto, DetalleMovimiento

admin.site.register(Editorial)
admin.site.register(Autor)
admin.site.register(Producto)
admin.site.register(Bodega)
admin.site.register(MovimientoProducto)
admin.site.register(DetalleMovimiento)

