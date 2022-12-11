from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index, name='index'),
    path('about/', views.About, name='about'),
    path('hello/<str:username>', views.Hello, name='hello'),
    path('projects/', views.Projects, name='projects'),
    path('projects/<int:id>', views.project_detail, name='project_detail'),
    path('tasks/', views.Tasks, name='tasks'),
    path('create_task/', views.create_task, name='create_task'),
    path('create_project/', views.create_project, name='create_project')
]
