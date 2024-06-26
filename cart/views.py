from django.shortcuts import render
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Item, Cart, ElementoCarrito
from django.contrib.auth.models import User
from .models import Cart

#receiver vendría a ser como un "evento", cada vez que se crea un usuario se crea un Cart
# asociado a ese usuario de modo que cada usuario tiene su propio carrito
@receiver(post_save, sender=User)
def crear_carrito(sender, instance, created, **kwargs):
    if created:
        Cart.objects.create(usuario=instance)

def thankyou(request):
    return render(request, 'cart/thankyou.html',)

#metodo que accede al checkout, se multiples operaciones para calcular 
# total del carrito y subtotal de cada item(item x cantidad)
@login_required
def checkout(request):
    carrito = get_object_or_404(Cart, usuario=request.user)
    elementos = carrito.elementos.all()
    
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

#agrega al carrito el item en cuestión o le suma 1 a la cantidad si ya existe
@login_required
def agregar_al_carrito(request, prenda_id):
    prenda = get_object_or_404(Item, id=prenda_id)
    carrito, created = Cart.objects.get_or_create(usuario=request.user)
    elemento, created = ElementoCarrito.objects.get_or_create(carrito=carrito, prenda=prenda)

    #verifica que no esté creado ya, si esta creado(false) se le suma +1 a la cantidad
    if not created:
        elemento.cantidad += 1
        elemento.save()
    return redirect('ver_carrito')

#lo mismo que el método anterior pero resta uno a la cantidad siempre que la cantidad
# sea mayor que uno en caso de ser 1 o menor que 1, se elimina el Elemento del carrito
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

#metodo para mostrar el carrito, calcula el total del carrito y se lo pasa al html
@login_required
def ver_carrito(request):
    carrito = get_object_or_404(Cart, usuario=request.user)
    elementos = carrito.elementos.all()
    total = sum(elemento.prenda.precio * elemento.cantidad for elemento in elementos)
    return render(request, 'cart/cart.html', {'carrito': carrito, 'total': total})

#elimina el elemento del carrito independientemente de la cantidad de items
@login_required
def eliminar_del_carrito(request, elemento_id):
    elemento = get_object_or_404(ElementoCarrito, id=elemento_id)
    elemento.delete()
    return redirect('ver_carrito')