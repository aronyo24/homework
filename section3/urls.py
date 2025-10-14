from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [
   path('section3/', views.section3_view, name='section3'),
]
