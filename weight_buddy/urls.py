from django.urls import path
from . import views

urlpatterns = [
    path('', views.weight_list, name='weight_list'),
]