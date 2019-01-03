from django.urls import path
from . import views

urlpatterns = [    
    
    path('', views.workout_list, name='workout_list'),
    path('exercises/', views.exercises_list , name='exercises_list'),
    path('training/<int:pk>/', views.workout_detail, name='workout_detail'),
    path('training/new', views.training_new, name='training_new'),
    path('training/<int:pk>/edit/', views.training_edit, name='training_edit'),



]