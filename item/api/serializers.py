from item.models import Category, Item
from rest_framework import serializers


class CategorySerializer(serializers.ModelSerializer):
    """Category serializer."""

    class Meta:
        model = Category
        fields = ["name"]


class ItemSerializer(serializers.ModelSerializer):
    """Item serializer."""

    class Meta:
        model = Item
        fields = [
            "category",
            "name",
            "description",
            "price",
            "is_sold",
            "created_by",
            "created_at",
        ]
