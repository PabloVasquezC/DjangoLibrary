from django.shortcuts import render
from myapp.models import Editorial
from django.http import HttpResponse

def hello_world(request):
    return HttpResponse("Welcome to Bodegas de libros blabla")


def publishers(request):
    editoriales = Editorial.objects.all()  # Recupera todas las editoriales
    return render(request, 'myapp/publishers.html', {'editoriales': editoriales})
