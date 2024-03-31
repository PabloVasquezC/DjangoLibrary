from django.shortcuts import render
from myapp.models import Editorial
from django.http import HttpResponse



def publishers(request):
    editoriales = Editorial.objects.all()  # Recupera todas las editoriales
    return render(request, 'myapp/publishers.html', {'editoriales': editoriales})


def home(request):
    return render(request, 'myapp/base.html', {'app_name': 'myapp'})