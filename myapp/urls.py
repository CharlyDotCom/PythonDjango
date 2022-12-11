from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index),
    path('about/', views.About),
    path('hello/<str:username>', views.Hello),
    path('projects/', views.Projects),
    path('tasks/', views.Tasks),
    path('create_task/', views.create_task),
    path('create_project/', views.create_project)
]
