from item.models import Category,Item
from rest_framework import serializers

class CategorySerialiZer(serializers.ModelSerializer):
     
    class Meta:
        model = Category
        fields = ["name"]
        
class ItemSerializer(serializers.ModelSerializer):
    
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