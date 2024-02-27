from django import forms
from django.core.exceptions import ValidationError

from .models import ContactUser

def validate_checked(value):
    if not value:
        raise ValidationError("Required.")

class ContactUsForm(forms.Form):
    class Meta:
        model = ContactUser
        fields = (
            'first_name', 'last_name', 'email', 'subject', 'message'
        )
        widgets = {
            'first_name': forms.TextInput(attrs={'autofocus': True}),
            'email': forms.EmailInput(
                attrs = {'placeholder':'you@example.com'}
            ),
            'message': forms.Textarea(attrs={'cols': '100', 'rows': '5'})
        }