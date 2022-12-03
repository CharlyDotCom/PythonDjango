from django.urls import path
from . import views

urlpatterns = [
    path('', views.Hello),
    path('about/', views.About)
]
