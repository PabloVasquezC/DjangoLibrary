from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class Editorial(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Autor(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Bodega(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=255)

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

    nombre = models.CharField(max_length=255, default='Sin nombre')
    tipo = models.CharField(max_length=2, choices=TIPO_OPCIONES, default=LIBRO)
    editorial = models.ForeignKey(Editorial, on_delete=models.PROTECT)
    autores = models.ManyToManyField(Autor)
    descripcion = models.TextField()
    precio_venta = models.DecimalField(max_digits=10, decimal_places=2)
    precio_arriendo = models.DecimalField(max_digits=10, decimal_places=2)
    fotoLink = models.TextField(max_length=1000000)
    bodega = models.ForeignKey(Bodega, on_delete=models.PROTECT)
    cantidad_en_stock = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.nombre

    def clean(self):
        if self.precio_venta <= 0:
            raise ValidationError({'precio_venta': 'El precio de venta debe ser un valor positivo.'})
        if self.precio_arriendo <= 0:
            raise ValidationError({'precio_arriendo': 'El precio de arriendo debe ser un valor positivo.'})


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

class Transaccion(models.Model):
    COMPRA = 'C'
    ARRIENDO = 'A'
    TIPO_TRANSACCION = [
        (COMPRA, 'Compra'),
        (ARRIENDO, 'Arriendo'),
    ]

    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    tipo = models.CharField(max_length=1, choices=TIPO_TRANSACCION)
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.get_tipo_display()} - {self.usuario.username} - {self.fecha}"

class DetalleTransaccion(models.Model):
    transaccion = models.ForeignKey(Transaccion, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.transaccion} - {self.producto.nombre} - {self.cantidad}"

from django.test import TestCase
from django.contrib.auth.models import User
from .models import Producto, Editorial, Bodega, Transaccion, DetalleTransaccion

class TransaccionIntegrationTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.editorial = Editorial.objects.create(nombre='Editorial Test')
        self.bodega = Bodega.objects.create(nombre='Bodega Test', direccion='Dirección Test')
        self.producto = Producto.objects.create(
            nombre='Producto Test',
            tipo='LB',
            editorial=self.editorial,
            descripcion='Descripción Test',
            precio_venta=100,
            precio_arriendo=50,
            fotoLink='http://test.com/image.jpg',
            bodega=self.bodega,
            cantidad_en_stock=10
        )
        self.transaccion = Transaccion.objects.create(
            usuario=self.user,
            tipo='C',
            total=100
        )
        self.detalle_transaccion = DetalleTransaccion.objects.create(
            transaccion=self.transaccion,
            producto=self.producto,
            cantidad=1,
            precio=100
        )

    def test_creacion_transaccion(self):
        self.assertEqual(Transaccion.objects.count(), 1)
        self.assertEqual(DetalleTransaccion.objects.count(), 1)
        self.assertEqual(self.producto.cantidad_en_stock, 9)

