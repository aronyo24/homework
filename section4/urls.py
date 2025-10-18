from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [
   path('section4/', views.section4_view, name='section4'),
]
