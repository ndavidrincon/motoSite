from rest_framework.serializers import ModelSerializer
from .models import ProductGuerrero


class productSerializer(ModelSerializer):
    class Meta:
        model = ProductGuerrero
        fields = [
            "name",
            "description",
            "price",
            "photo",
        ]
