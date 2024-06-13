from django.shortcuts import render
from .models import Item

def home(request):
    return render(request, 'tienda_app/index.html',)

def shop(request):
    prendas = Item.objects.all().order_by('categoria')
    return render(request, 'tienda_app/shop.html', {'prendas': prendas})

def about(request):
    return render(request, 'tienda_app/about.html',)

def contact(request):
    return render(request, 'tienda_app/contact.html',)

def checkout(request):
    return render(request, 'cart/checkout.html',)