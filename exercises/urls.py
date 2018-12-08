from django.urls import path
from . import views

urlpatterns = [
    path('', views.exercises_list, name='exercises_list'),
]