from django.contrib import admin
from django.urls import include, path

from . import views 
urlpatterns = [
  path('section2/', views.section2_view, name='section2'),
]
