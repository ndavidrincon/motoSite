from django.urls import reverse_lazy
from django.views import generic
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response

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


class ProductListAPI(APIView):
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        products = ProductGuerrero.objects.all()
        serializer = productSerializer(products, many=True)
        return Response(serializer.data)
