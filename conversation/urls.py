from django.urls import path

from . import views

app_name = 'conversation'

urlpatterns = [
    path('inbox/', views.inbox, name='inbox'),
    path('<int:pk>/', views.detail, name='details'),
    path('new/<int:item_pk>/', views.new_conversation, name='new'),
]