from django.urls import reverse_lazy
from django.views import generic

from ventasGuerrero.models import ProductGuerrero
from .forms import VentasGuerreroForm

class VentasGuerreroFormView(generic.FormView):
    template_name = "products/add_product.html"
    form_class = VentasGuerreroForm
    success_url = reverse_lazy("add_product")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
class ProductListView(generic.ListView):
    model = ProductGuerrero
    template_name = 'products/list_products.html'
    context_object_name = 'products'
    