from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [    
    
    path('', views.home_page, name='home_page'),

    path('exercises/', views.exercise_list , name='exercise_list'),
    path('exercises/<slug:slug>-<int:pk>/', views.exercise_detail, name='exercise_detail'),
    path('exercises/new', views.exercise_new, name='exercise_new'),
    path('exercises/<slug:slug>-<int:pk>/edit/', views.exercise_edit, name='exercise_edit'),
    
    path('contact/', views.contact_page, name='contact_page'),
    path('about/', views.about_page, name='about_page'),

    path('upload-csv/', views.exercises_upload, name="exercises_upload"),

    path('blog/', views.post_list, name='post_list'),
    path('blog/post/<int:pk>/', views.post_detail, name='post_detail'),
    path('blog/post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('blog/post/new/', views.post_new, name='post_new'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
