from django.db import models
from django.contrib.auth.models import User

class Editorial(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Autor(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    LIBRO = 'LB'
    REVISTA = 'RV'
    ENCICLOPEDIA = 'EN'
    TIPO_OPCIONES = [
        (LIBRO, 'Libro'),
        (REVISTA, 'Revista'),
        (ENCICLOPEDIA, 'Enciclopedia'),
    ]

    tipo = models.CharField(max_length=2, choices=TIPO_OPCIONES, default=LIBRO)
    editorial = models.ForeignKey(Editorial, on_delete=models.PROTECT)
    autores = models.ManyToManyField(Autor)
    descripcion = models.TextField()
    # cantidad_en_stock = models.PositiveIntegerField() # Opcional

    def __str__(self):
        return f"{self.get_tipo_display()} - {self.editorial.nombre}"

class Bodega(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre

class MovimientoProducto(models.Model):
    bodega_origen = models.ForeignKey(Bodega, related_name='movimientos_origen', on_delete=models.CASCADE)
    bodega_destino = models.ForeignKey(Bodega, related_name='movimientos_destino', on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_movimiento = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"De {self.bodega_origen} a {self.bodega_destino} - {self.fecha_movimiento}"

class DetalleMovimiento(models.Model):
    movimiento = models.ForeignKey(MovimientoProducto, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()

    def __str__(self):
        return f"{self.producto} - Cantidad: {self.cantidad}"
