from django import forms
from .models import Contact

class Contact_form(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ["full_name","email","phone_number","message"]
        widgets = {
            "full_name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Nombre completo"}),
            "email": forms.EmailInput(attrs={"class": "form-control", "placeholder": "Email"}  ),
            "phone_number": forms.TextInput(attrs={"class": "form-control", "placeholder": "Número de teléfono"}),
            "message": forms.TextInput(attrs={"class": "form-control message-box mb-5", "placeholder": "Contenido"}  ),
        }