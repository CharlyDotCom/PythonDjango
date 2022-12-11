from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index),
    path('about/', views.About),
    path('hello/<str:username>', views.Hello),
    path('projects/', views.Projects),
    path('tasks/<int:id>', views.Tasks)
]
