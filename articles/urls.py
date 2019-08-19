from django.urls import path
# 현재 app(directory)의 views.py
from . import views

urlpatterns = [
   path('', views.index),
   path('new/', views.new),
   path('create/', views.create),
]
 