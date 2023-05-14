from django.urls import path
from django.conf.urls import handler404
from . import views

urlpatterns = [
    path('', views.main, name='home'),
    
    path('main/', views.main, name='main'),
    path('main_correct/', views.main_correct, name='main_correct'),  
    path('main_incorrect/', views.main_incorrect, name='main_incorrect'), 

    path('prog/', views.prog, name='prog'),
    path('prog_correct/', views.prog_correct, name='prog_correct'),  
    path('prog_incorrect/', views.prog_incorrect, name='prog_incorrect'), 

    path('tv/', views.tv, name='tv'),
    path('tv_correct/', views.tv_correct, name='tv_correct'),  
    path('tv_incorrect/', views.tv_incorrect, name='tv_incorrect'),   

    path('book/', views.book, name='book'),
    path('book_correct/', views.book_correct, name='book_correct'),  
    path('book_incorrect/', views.book_incorrect, name='book_incorrect'),   

    path('404/', views.handler404, name='handler404'),    
]