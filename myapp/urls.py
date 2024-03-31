from . import views
from django.urls import path
from .views import hello_world,  publishers

urlpatterns = [
    path('', hello_world, name='hello_world'),
    path('publishers/', views.publishers, name='publishers')

]
