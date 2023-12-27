
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from item.models import Item

@login_required
def index(request):
    items = Item.objects.all()

    return render(request, 'dashboard.html', {'items': items})