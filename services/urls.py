from django.urls import path
from services import views

urlpatterns = [
    path('services/', views.services, name='servicios')
]