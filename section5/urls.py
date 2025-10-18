from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [
   path('section5/', views.section5_view, name='section5'),
]
