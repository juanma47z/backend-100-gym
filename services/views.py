from django.shortcuts import render, get_object_or_404
from .models import Services

def services(request):
    service = Services.objects.all()
    return render(request, 'services/services.html', {'service': service})
