from django.contrib import admin
from django.urls import include, path
from . import views 

urlpatterns = [
   path('', views.index, name='home'),
   path('section1/', views.section1_view, name='section1'),
]
