from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import View
from django.shortcuts import render, redirect

class RegisterView(View):
    def get(self, request):
        form = UserCreationForm()
        return render(request, 'registrationN/register.html', {'form': form})
    
    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        return render(request, 'registrationN/register.html', {'form': form})
