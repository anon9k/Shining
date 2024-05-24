from django.shortcuts import render

def home(request):
    return render(request, 'tienda_app/index.html',)

def shop(request):
    return render(request, 'tienda_app/shop.html',)

def about(request):
    return render(request, 'tienda_app/about.html',)

def contact(request):
    return render(request, 'tienda_app/contact.html',)

def cart(request):
    return render(request, 'tienda_app/cart.html',)

def checkout(request):
    return render(request, 'tienda_app/checkout.html',)