# Generated by Django 5.0.3 on 2024-08-06 14:03

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Bodega',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('direccion', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Editorial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='MovimientoProducto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_movimiento', models.DateTimeField(auto_now_add=True)),
                ('bodega_destino', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movimientos_destino', to='myapp.bodega')),
                ('bodega_origen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movimientos_origen', to='myapp.bodega')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(default='Sin nombre', max_length=255)),
                ('tipo', models.CharField(choices=[('LB', 'Libro'), ('RV', 'Revista'), ('EN', 'Enciclopedia')], default='LB', max_length=2)),
                ('descripcion', models.TextField()),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('fotoLink', models.TextField(max_length=1000000)),
                ('autores', models.ManyToManyField(to='myapp.autor')),
                ('editorial', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='myapp.editorial')),
            ],
        ),
        migrations.CreateModel(
            name='DetalleMovimiento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('movimiento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.movimientoproducto')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.producto')),
            ],
        ),
    ]
