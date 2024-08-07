from django.db.models import Count
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_protect
from .models import Editorial, Producto, Bodega
import json
from .forms import CustomUserCreationForm  
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout





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
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request, user)
                messages.info(request, f"Bienvenido/a, {username}")
                return redirect('home')
            else:
                messages.error(request, "Nombre de usuario o contraseña no válido.")
        else:
            messages.error(request, "Información inválida.")
    else:
        form = AuthenticationForm()
    return render(request, 'myapp/login.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cuenta creada exitosamente. Ahora puedes iniciar sesión.')
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'myapp/register.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('home')



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
