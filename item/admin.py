from django.contrib import admin
from .models import Item,User

from .models import Category

admin.site.register(Category)
admin.site.register(Item)
admin.site.register(User)