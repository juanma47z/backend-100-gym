from django.urls import path
from core import views

urlpatterns = [
    path('home/', views.home, name='casa'),
    path('about/', views.about, name='historia'),
    path('store/', views.store, name='visitanos')
]