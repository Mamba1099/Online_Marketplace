from django.urls import path

from item.api import views

urlpatterns = [
    path("category/", views.CategoryList.as_view()),
    path("category/<int:pk>/", views.CategoryDetail.as_view()),
    path("item/", views.ItemList.as_view()),
    path("item/<int:pk>/", views.ItemDetail.as_view()),
]
