from rest_framework import serializers

from .models import Category, Sneaker


class SneakerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sneaker
        fields = (
            "id",
            "name",
            "get_absolute_url",
            "description",
            "price",
            "get_image",
            "get_thumbnail",
        )


class CategorySerializer(serializers.ModelSerializer):
    sneakers = SneakerSerializer(many=True)

    class Meta:
        model = Category
        fields = (
            "id",
            "name",
            "get_absolute_url",
            "sneakers",
        )
