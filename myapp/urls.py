from . import views
from django.urls import path
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.home, name='home'),
    path('publishers/', views.publishers, name='publishers'),
    path('catalog/', views.catalog, name='catalog'),
    path('warehouses/', views.warehouses, name='warehouses'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('confirmar_pago/', views.confirmar_pago, name='confirmar_pago'),
    path('actualizar-stock/', views.actualizar_stock, name='actualizar_stock'),  
    path('register/', views.register, name='register'),



]
