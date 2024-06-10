from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import ContactForm
from .models import Contact

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            
            Contact.objects.create(
                name = form.cleaned_data['name'],
                email = form.cleaned_data['email'],
                content = form.cleaned_data['content']
            )
            
            return redirect(reverse('contacto') + "?ok")
    else:
        form = ContactForm()

    return render(request, 'contact/contact.html', {'form': form})
