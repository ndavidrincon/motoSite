from django.db import models


class ProductGuerrero(models.Model):
    tipe_1 = "1"
    tipe_2 = "2"
    tipe_3 = "3"

    tipo_choises = [
        (tipe_1, 'Motos'),
        (tipe_2, 'Tienda'),
        (tipe_3, 'Pulguero de Guerrero'),
    ]

    name = models.TextField(max_length=200, verbose_name="Nombre producto")
    description = models.TextField(max_length=250, verbose_name="Descripción")
    price = models.DecimalField(max_digits=10, decimal_places=0, verbose_name="Precio")
    tipe = models.CharField(
        max_length=1,
        choices=tipo_choises,
        default=tipe_1,
        verbose_name="Tipo de producto"
    )
    photo = models.ImageField(
        upload_to="Logos", null=True, blank=True, verbose_name="Imagen"
    )

    def __str__(self):
        return self.name
