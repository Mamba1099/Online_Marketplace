from django.urls import path

from item.api.urls import urlpatterns as api_urlpatterns
from item import views

app_name = "item"

urlpatterns = [
    path("", views.items, name="items"),
    path("new/", views.new, name="new"),
    path("<int:pk>/", views.detail, name="detail"),
    path("<int:pk>/delete/", views.delete, name="delete"),
    path("<int:pk>/edit/", views.edit, name="edit"),
]

urlpatterns += api_urlpatterns
