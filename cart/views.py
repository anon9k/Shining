from django.shortcuts import render
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Item, Cart, ElementoCarrito
from django.contrib.auth.models import User
from .models import Cart

@login_required
def cart(request):
    return render(request, 'cart/cart.html',)

def thankyou(request):
    return render(request, 'cart/thankyou.html',)

@login_required
def checkout(request):
    carrito = get_object_or_404(Cart, usuario=request.user)
    elementos = carrito.elementos.all()
    
    # Lista para almacenar los elementos con sus subtotales
    elementos_con_subtotales = []
    total = 0

    for elemento in elementos:
        subtotal = elemento.prenda.precio * elemento.cantidad
        total += subtotal
        elementos_con_subtotales.append({
            'prenda': elemento.prenda,
            'cantidad': elemento.cantidad,
            'subtotal': subtotal
        })

    return render(request, 'cart/checkout.html', {
        'elementos': elementos_con_subtotales,
        'total': total
    })

@receiver(post_save, sender=User)
def crear_carrito(sender, instance, created, **kwargs):
    if created:
        Cart.objects.create(usuario=instance)

@login_required
def agregar_al_carrito(request, prenda_id):
    prenda = get_object_or_404(Item, id=prenda_id)
    carrito, created = Cart.objects.get_or_create(usuario=request.user)
    elemento, created = ElementoCarrito.objects.get_or_create(carrito=carrito, prenda=prenda)

    if not created:
        elemento.cantidad += 1
        elemento.save()
    return redirect('ver_carrito')

@login_required
def quitar_unidad_al_carrito(request, prenda_id):
    prenda = get_object_or_404(Item, id=prenda_id)
    carrito = get_object_or_404(Cart, usuario=request.user)
    elemento = get_object_or_404(ElementoCarrito, carrito=carrito, prenda=prenda)

    if elemento.cantidad > 1:
        elemento.cantidad -= 1
        elemento.save()
    else:
        elemento.delete()

    return redirect('ver_carrito')

@login_required
def ver_carrito(request):
    carrito = get_object_or_404(Cart, usuario=request.user)
    elementos = carrito.elementos.all()
    total = sum(elemento.prenda.precio * elemento.cantidad for elemento in elementos)
    return render(request, 'cart/cart.html', {'carrito': carrito, 'total': total})

@login_required
def eliminar_del_carrito(request, elemento_id):
    elemento = get_object_or_404(ElementoCarrito, id=elemento_id)
    elemento.delete()
    return redirect('ver_carrito')