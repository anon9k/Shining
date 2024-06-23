from django.db import models
from django.contrib.auth.models import User
from tienda_app.models import Item

class Cart(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Carrito de {self.usuario.username}"

class ElementoCarrito(models.Model):
    carrito = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='elementos')
    prenda = models.ForeignKey(Item, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.cantidad} x {self.prenda.nombre}"