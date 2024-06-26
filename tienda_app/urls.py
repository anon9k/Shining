
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name= 'home'),
    path('shop/', views.shop, name = 'shop'),
    path('about/', views.about, name = 'about'),
    path('contact/', views.contact, name = 'contact'),
]