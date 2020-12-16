from django.urls import path
<<<<<<< HEAD
from . import views

app_name = 'articles'

urlpatterns = [
   path('', views.index, name='index'),
   # path('new/', views.new, name='new'),
   path('create/', views.create, name='create'),
   path('<int:article_pk>/', views.detail, name='detail'),
   path('<int:article_pk>/delete/', views.delete, name='delete'),
   # path('<int:article_pk>/edit/', views.edit, name='edit'),
   path('<int:article_pk>/update/', views.update, name='update'),
   path('<int:article_pk>/comment_create/', views.comment_create, name='comment_create'),
   path('<int:article_pk>/comment_create/<int:comment_pk>/comment_delete/', views.comment_delete, name='comment_delete'),
]
=======
# 현재 app(directory)의 views.py
from . import views

urlpatterns = [
   path('', views.index),
   path('new/', views.new),
   path('create/', views.create),
]
 
>>>>>>> django_crud/master
