from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [    
    
    path('', views.home_page, name='home_page'),

    path('exercises/', views.exercise_list , name='exercise_list'),
    path('exercises/<int:pk>/', views.exercise_detail, name='exercise_detail'),
    path('exercises/new', views.exercise_new, name='exercise_new'),
    path('exercises/<int:pk>/edit/', views.exercise_edit, name='exercise_edit'),
    
    path('contact/', views.contact_page, name='contact_page'),
    path('about/', views.about_page, name='about_page'),

    path('upload-csv/', views.exercises_upload, name="exercises_upload"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
