from django.contrib import admin
from django.urls import path
from . import views



urlpatterns = [
    path('',views.home,name='home'),
    # path('upload/', views.upload_coffee, name='upload_coffee'),
    # path('success/', views.success, name='success'),


  
]
