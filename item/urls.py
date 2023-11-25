from django.urls import path
from .import views

app_name = 'item'

urlpatterns = [
    path('detail/<int:id>/', views.details, name='detail'),

]