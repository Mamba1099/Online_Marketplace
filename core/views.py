from django.shortcuts import render

from item.models import Category, Item
from .forms import SignUpForm   


def index(request):
    items = Item.objects.filter(is_sold=False)[0:6]
    categories = Category.objects.all()

    return render(request, "index.html", {"items": items, "categories": categories})


def contact(request):
    return render(request, "contact.html")

"""initialize instance for SignUpForm"""
def signup(request):
    form = SignUpForm()
    
    return render(request, "signup.html", {
        'form': form 
})