from . import views
from django.urls import path


urlpatterns = [
    path('', views.home, name='home'),
    path('publishers/', views.publishers, name='publishers'),
    path('catalog/', views.catalog, name='catalog'),
    path('warehouses/', views.warehouses, name='warehouses'),
    path('cart/', views.cart, name='cart'),


]
