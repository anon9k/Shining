from django.urls import path
from . import views

urlpatterns = [
    path('agregar/<int:prenda_id>/', views.agregar_al_carrito, name='agregar_al_carrito'),
    path('cart/', views.ver_carrito, name='ver_carrito'),
    path('eliminar/<int:elemento_id>/', views.eliminar_del_carrito, name='eliminar_del_carrito'),
    path('', views.cart, name = 'cart'),
    path('checkout/', views.checkout, name='checkout'),

]