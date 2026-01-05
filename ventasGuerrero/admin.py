from django.contrib import admin
from ventasGuerrero.models import ProductGuerrero


class ProductGuerreroAdmin(admin.ModelAdmin):
    model = ProductGuerrero
    list_display = ["name", "price"]
    search_fields = ["name", "price"]


admin.site.register(ProductGuerrero, ProductGuerreroAdmin)
