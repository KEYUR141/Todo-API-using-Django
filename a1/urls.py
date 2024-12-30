from django.contrib import admin
from django.urls import path
from .views import *
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views

router = DefaultRouter()
router.register(r'todo-view-set', TodoViewSet, basename='todo')


urlpatterns = [
   path('', home,name='home'),
   path('post-todo/',postTodo,name='postTodo'),
   path('get-todo/',getTodo,name='getTodo'),
   path('patch-todo/',patchTodo,name='patchTodo'),

   path('todo/',TodoView.as_view()),
] 
urlpatterns += router.urls

