from django.db import models

class ProductGuerrero (models.Model):
    name = models.TextField(max_length=200, verbose_name="Nombre producto")
    description = models.TextField(max_length=250, verbose_name="Descripción")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Precio")
    photo = models.ImageField(upload_to="Logos", null= True, blank=True, verbose_name="Imagen")

    def __str__(self):
        return self.name
