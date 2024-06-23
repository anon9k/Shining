from django.db import models

class Item(models.Model ):
    nombre = models.CharField(max_length=100)
    precio = models.IntegerField(default=999)
    stock = models.IntegerField(default=0)
    opciones_categoria = [
       ('CA', 'Camiseta'),
       ('SU', 'Sudadera'),
       ('PA', 'Pantalon'),
       ('AB','Abrigo'),
    ]
    categoria = models.CharField(max_length=20, choices=opciones_categoria, default="Nombre prenda")
    imagen = models.ImageField(null=True, blank=True, upload_to='images/')

    
    def __str__(self):
      return f'{self.nombre} - ID: {self.id} - Stock: {self.stock}'