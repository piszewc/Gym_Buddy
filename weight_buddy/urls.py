from django.urls import path
from . import views

urlpatterns = [
    path('', views.weight_list, name='weight_list'),
    path('training/<int:pk>/', views.weight_detail, name='weight_detail'),
    path('training/new', views.training_new, name='training_new'),
    path('training/<int:pk>/edit/', views.training_edit, name='training_edit'),

    path('', views.exercises , name='exercises'),


]