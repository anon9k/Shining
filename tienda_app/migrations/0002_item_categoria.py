# Generated by Django 5.0.6 on 2024-06-05 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='categoria',
            field=models.CharField(choices=[('CA', 'Camiseta'), ('SU', 'Sudadera'), ('PA', 'Pantalon'), ('AB', 'Abrigo')], default='Nombre prenda', max_length=20),
        ),
    ]
