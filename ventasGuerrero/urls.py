from django.urls import path
from .views import ProductListView, ProductListViewTipe, VentasGuerreroFormView, ProductListAPI

urlpatterns = [
    path("", ProductListView.as_view(), name="list_product"),
    path("tipo_productos/", ProductListViewTipe.as_view(
        template_name="products/tipe_product.html"
    ), name="tipe_product"),
    path("productos/<str:tipe>/", ProductListViewTipe.as_view(), name="list_product_tipe"),
    path("api/", ProductListAPI.as_view(), name="list_product_api"),
    path("agregar/", VentasGuerreroFormView.as_view(), name="add_product"),
]
