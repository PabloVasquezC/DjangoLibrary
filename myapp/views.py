from django.db.models import Count
from django.shortcuts import render
from myapp.models import Editorial, Producto
from django.http import HttpResponse




def home(request):
    # Añade una ruta de imagen específica para la vista de home
    hero_image = 'images/heroHome.jpg'
    return render(request, 'myapp/base.html', {
        'app_name': 'myapp',
        'hero_image': hero_image
    })

def publishers(request):
    editoriales = Editorial.objects.all()  # Su consulta original
    # Realiza una consulta separada para obtener la cantidad de productos por editorial
    info_editoriales = Editorial.objects.annotate(cantidad_productos=Count('producto'))
    hero_image = 'images/heroPublisher.jpg'
    return render(request, 'myapp/publishers.html', {
        'editoriales': editoriales,
        'info_editoriales': info_editoriales,  # Agregue el nuevo contexto aquí
        'hero_image': hero_image
    })

def catalog(request):
    productos = Producto.objects.all()
    return render(request, 'myapp/catalog.html',{'productos': productos})