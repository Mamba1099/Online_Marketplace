
# from django.shortcuts import render, get_object_or_404, redirect
# from django.contrib.auth.decorators import login_required

# from django.db.models import Q
# from .forms import NewItemForm, EditItemForm
# from .models import Item, Category


# def items(request):
#     query = request.GET.get('query', '')
#     category_id = request.GET.get('category', 0)
#     categories = Category.objects.all()
#     items = Item.objects.filter(is_sold=False)

#     if category_id:
#         items = items.filter(category_id=category_id)

#     if query:
#         items = items.filter(Q(name__icontains=query) | Q(description__icontains=query))

#     return render(request, 'items.html', {
#         'items': items,
#         'query': query,
#         'categories': categories,
#         'category_id': int(category_id)
#     })

# """display detail for item identified by pk"""
# def detail(request, pk):
#     item = get_object_or_404(Item, pk=pk)
#     related_items = Item.objects.filter(category=item.category, is_sold=False).exclude(pk=pk)[0:3]

#     return render(request, 'details.html', {
#         'item': item,
#         'related_items': related_items
#     })

# @login_required
# def new(request):
#     if request.method == 'POST':
#         form = NewItemForm(request.POST, request.FILES)

#         if form.is_valid():
#             item = form.save(commit=False)
#             item.created_by = request.user
#             item.save()

#             return redirect('item:detail', pk=item.id)
#     else:
#         form = NewItemForm()

#     return render(request, 'form.html', {
#         'form': form,
#         'title': 'New item',
#     })

# @login_required
# def edit(request, pk):
#     item = get_object_or_404(Item, pk=pk, created_by=request.user)

#     if request.method == 'POST':
#         form = EditItemForm(request.POST, request.FILES, instance=item)

#         if form.is_valid():
#             form.save()

#             return redirect('item:detail', pk=item.id)
#     else:
#         form = EditItemForm(instance=item)

#     return render(request, 'form.html', {
#         'form': form,
#         'title': 'Edit item',
#     })

# @login_required
# def delete(request, pk):
#     item = get_object_or_404(Item, pk=pk, created_by=request.user)
#     item.delete()

#     return redirect('index.html')

from item.serializers import CategorySerialiZer,ItemSerializer
from item.models import Category,Item
from rest_framework import generics 

"""create a generic class to create the category model view"""
class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerialiZer

class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerialiZer

"""create a generic class to create the Item model view"""
class ItemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class ItemList(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer    