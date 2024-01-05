from item.models import Category,Item,User
from rest_framework import serializers

class CategorySerializer(serializers.ModelSerializer):
     
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
        
class UserSerializer(serializers.ModelSerializer):
  
    class Meta:
        model = User
        fields = [ "username", "email" ,"password"]