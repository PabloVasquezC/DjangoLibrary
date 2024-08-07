from django.db.models import Count
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_protect
from .models import Editorial, Producto, Bodega
import json
from .forms import CustomUserCreationForm  
from django.shortcuts import render, redirect



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
    return render(request, 'myapp/catalog.html', {
        'productos': productos,
    })

def warehouses(request):
    bodegas = Bodega.objects.all()  
    info_bodega = Bodega.objects.annotate(cantidad_productos=Count('nombre'))
    return render(request, 'myapp/warehouses.html', {
        'bodega': bodegas,
        'info_bodega': info_bodega,  
    })

def login(request):
    return render(request, 'myapp/login.html', {
        'app_name': 'myapp',    
    })

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # Opcional: iniciar sesión del usuario después del registro
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'myapp/register.html', {'form': form})



@csrf_protect
def actualizar_stock(request):
    if request.method == "POST":
        data = json.loads(request.body)
        product_id = data.get('product_id')
        action = data.get('action')
        product = get_object_or_404(Producto, id=product_id)

        if product.cantidad_en_stock > 0:
            product.cantidad_en_stock -= 1
            product.save()
            return JsonResponse({"success": True, "stock": product.cantidad_en_stock})
        else:
            return JsonResponse({"success": False, "error": "El producto no está disponible en stock."})
    return JsonResponse({"success": False, "error": "Método no permitido."})
