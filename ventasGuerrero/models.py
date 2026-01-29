import sys
from io import BytesIO
from PIL import Image
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.db import models


class ProductGuerrero(models.Model):
    MOTOS = "1"
    TIENDA = "2"
    PULGUERO = "3"

    TIPO_CHOICES = [
        (MOTOS, 'Motos'),
        (TIENDA, 'Tienda'),
        (PULGUERO, 'Pulguero de Guerrero'),
    ]

    name = models.CharField(max_length=200, verbose_name="Nombre producto")
    description = models.TextField(max_length=250, verbose_name="Descripción")
    price = models.DecimalField(max_digits=10, decimal_places=0, verbose_name="Precio")
    tipe = models.CharField(
        max_length=1, 
        choices=TIPO_CHOICES, 
        default=MOTOS, 
        verbose_name="Tipo de producto"
    )
    photo = models.ImageField(
        upload_to="Logos", 
        null=True, 
        blank=True, 
        verbose_name="Imagen"
    )

    def save(self, *args, **kwargs):
        # Solo optimiza si hay una foto y si es una subida nueva
        if self.photo and not self.photo._committed:
            self.photo = self.compress_image(self.photo)
        super().save(*args, **kwargs)

    def compress_image(self, photo):
        img = Image.open(photo)
        if img.mode != 'RGB':
            img = img.convert('RGB')

        output = BytesIO()
        img.thumbnail((800, 800)) # Ajusta según tu necesidad visual
        img.save(output, format='JPEG', quality=70, optimize=True)
        output.seek(0)

        return InMemoryUploadedFile(
            output, 'ImageField', f"{photo.name.split('.')[0]}.jpg",
            'image/jpeg', sys.getsizeof(output), None
        )

    def __str__(self):
        return self.name
