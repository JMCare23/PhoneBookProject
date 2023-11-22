from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    
    class Meta:
        model = Contact
        fields = '__all__'
        labels = {
            'name': 'name',
            'number': 'number',
            'email': 'email'
        }

