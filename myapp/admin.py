from django.contrib import admin
from .models import Editorial, Autor, Producto, Bodega, MovimientoProducto, DetalleMovimiento, Transaccion, DetalleTransaccion
from guardian.admin import GuardedModelAdmin


class ProjectAdmin(GuardedModelAdmin):
    pass

admin.site.register(Editorial, ProjectAdmin)
admin.site.register(Autor, ProjectAdmin)
admin.site.register(Producto, ProjectAdmin)
admin.site.register(Bodega, ProjectAdmin)
admin.site.register(MovimientoProducto, ProjectAdmin)
admin.site.register(DetalleMovimiento, ProjectAdmin)
admin.site.register(Transaccion, ProjectAdmin)
admin.site.register(DetalleTransaccion, ProjectAdmin)




