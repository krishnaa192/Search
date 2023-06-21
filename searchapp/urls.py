
from django.contrib import admin
from django.urls import path,include
from .import views

urlpatterns = [
   
    path('', views.search_dishes, name='search_dishes'),# urls for search page
]





