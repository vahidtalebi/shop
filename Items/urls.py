from django.urls import path
from . import views

urlpatterns = [
    path('api', views.itemList, name='item-list')
]
