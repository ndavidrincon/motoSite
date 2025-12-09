from django.urls import path
from .views import VentasGuerreroFormView

urlpatterns = [
    path('agregar/', VentasGuerreroFormView.as_view(), name="add_product"),
]