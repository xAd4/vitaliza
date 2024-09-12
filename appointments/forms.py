from django import forms
from .models import Appointment

class Appointment_form(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ["full_name","department","phone_number","symptoms"]
        widgets = {
            "full_name": forms.TextInput(attrs={"class":"form-control", "placeholder":"Nombre del paciente"}),
            "department": forms.Select(attrs={'class': 'form-control wide'}),
            "phone_number":forms.TextInput(attrs={"class":"form-control", "placeholder":"Teléfono del paciente"}),
            "symptoms":forms.TextInput(attrs={"class":"form-control", "placeholder":"Síntomas"}),
        }