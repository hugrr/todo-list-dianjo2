from django.contrib import admin
from django.urls import path, include
from api import views
urlpatterns = [
    path('todo/', views.TodoView.as_view(), name='id-todo'),
    #path('todo/', views.TodoView.as_view(), name='id-todo-usr'),
    path('todo/<int:todo_id>', views.TodoView.as_view(), name='id-todo-id')
]
