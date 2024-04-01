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
    editoriales = Editorial.objects.all()  # Recupera todas las editoriales
    # Añade una ruta de imagen específica para la vista de publishers
    hero_image = 'images/heroPublisher.jpg'
    return render(request, 'myapp/publishers.html', {
        'editoriales': editoriales,
        'hero_image': hero_image
    })


def catalog(request):
    productos = Producto.objects.all()
    return render(request, 'myapp/catalog.html',{'productos': productos})