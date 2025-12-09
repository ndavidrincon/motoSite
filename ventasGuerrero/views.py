from django.views import generic
from .forms import VentasGuerreroForm

class VentasGuerreroFormView(generic.FormView):
    template_name = "products/add_product.html"
    form_class = VentasGuerreroForm
