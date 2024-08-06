from django.db.models import Count
from django.shortcuts import render
from myapp.models import Editorial, Producto, Bodega
from django.http import HttpResponse




def home(request):
    hero_image = 'images/heroHome.jpg'
    return render(request, 'myapp/base.html', {
        'app_name': 'myapp',
        'hero_image': hero_image
    })

def publishers(request):
    editoriales = Editorial.objects.all()  
    info_editoriales = Editorial.objects.annotate(cantidad_productos=Count('producto'))
    return render(request, 'myapp/publishers.html', {
        'editoriales': editoriales,
        'info_editoriales': info_editoriales,  
    })

def catalog(request):
    productos = Producto.objects.all()
    return render(request, 'myapp/catalog.html',{
        'productos': productos,

    
    })

def warehouses(request):
    bodegas = Bodega.objects.all()  
    info_bodega = Bodega.objects.annotate(cantidad_productos=Count('nombre'))
    return render(request, 'myapp/warehouses.html', {
        'bodega': bodegas,
        'info_bodega': info_bodega,  
    })