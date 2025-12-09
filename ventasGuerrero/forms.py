from django import forms
from .models import ProductGuerrero

class VentasGuerreroForm(forms.Form):
    name = forms.CharField(max_length=200, required=True, label="Nombre")
    description = forms.CharField(max_length=250, required=True, label="Nombre")
    price = forms.DecimalField(max_digits=10, decimal_places=2, required=True, label="Precio")
    photo = forms.ImageField(label="Foto", required=False)

    def save(self):
        ProductGuerrero.objects.create(
            name = self.changed_data['name'],
            description = self.changed_data['description'],
            price = self.changed_data['price'],
            photo = self.changed_data[''],
        )
