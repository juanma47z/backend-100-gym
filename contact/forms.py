from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(
        label='Nombre', 
        required=True, 
        min_length=3, 
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Nombre', 'class': 'form-group'})
    )
    email = forms.EmailField(
        label='Email', 
        required=True,
        widget=forms.EmailInput(attrs={'placeholder': 'Email', 'class': 'form-group'})
    )
    content = forms.CharField(
        label='Contenido', 
        required=True,
        widget=forms.Textarea(attrs={'placeholder': 'Contenido', 'class': 'form-group'})
    )
