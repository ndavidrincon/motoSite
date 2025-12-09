from django.urls import path
from .views import ProductListView, VentasGuerreroFormView

urlpatterns = [
    path('', ProductListView.as_view(), name="list_product"),
    path('agregar/', VentasGuerreroFormView.as_view(), name="add_product"),
]