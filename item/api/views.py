from item.api.serializers import CategorySerializer, ItemSerializer,UserSerializer
from item.models import Category, Item,User
from rest_framework import generics


class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    """Category detail view."""

    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryList(generics.ListCreateAPIView):
    """Category list view."""

    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ItemDetail(generics.RetrieveUpdateDestroyAPIView):
    """Item detail view."""

    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class ItemList(generics.ListCreateAPIView):
    """Item list view."""

    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    
class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        serializer.save()
        