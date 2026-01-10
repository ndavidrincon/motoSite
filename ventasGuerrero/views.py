from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
from django.views.generic import ListView

from ventasGuerrero.models import ProductGuerrero
from .forms import VentasGuerreroForm
from .serializers import productSerializer


class VentasGuerreroFormView(generic.FormView):
    template_name = "products/add_product.html"
    form_class = VentasGuerreroForm
    success_url = reverse_lazy("add_product")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class ProductListView(generic.ListView):
    model = ProductGuerrero
    template_name = "products/list_products.html"
    context_object_name = "products"

class ProductListViewTipe(ListView):
    model = ProductGuerrero
    template_name = "products/list_products.html"
    context_object_name = "products"

    def get_queryset(self):
        tipe = self.kwargs.get("tipe")
        return ProductGuerrero.objects.filter(tipe=tipe)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        tipe = self.kwargs.get("tipe")
        context["tipe_name"] = dict(ProductGuerrero.tipo_choises).get(tipe)

        return context

class ProductListAPI(APIView):
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        products = ProductGuerrero.objects.all()
        serializer = productSerializer(products, many=True)
        return Response(serializer.data)
    

def productos_por_tipo(request, tipe):
    products = ProductGuerrero.objects.filter(tipe=tipe)
    return render(request, "products/list_products.html", {
        "products": products,
        "tipe": tipe
    })

