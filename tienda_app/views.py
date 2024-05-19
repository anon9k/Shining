from django.shortcuts import render

def home(request):
    return render(request, 'tienda_app/index.html',)

def shop(request):
    return render(request, 'tienda_app/shop.html',)

def about(request):
    return render(request, 'tienda_app/about.html',)

def about(request):
    return render(request, 'tienda_app/contact.html',)