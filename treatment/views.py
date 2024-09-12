from django.shortcuts import render
from django.urls import reverse_lazy
from django import forms
from django.utils.decorators import method_decorator
from django.contrib.admin.views.decorators import staff_member_required
from django.views.generic import DetailView, UpdateView
from .models import Treatment

# Create your views here.

class TreatmentDetailView(DetailView):
    template_name = "treatment/treatment_detail.html"
    model = Treatment
    context_object_name = "treatment"

@method_decorator(staff_member_required, name="dispatch")
class TreatmentUpdateView(UpdateView):
    model = Treatment
    template_name = "forms/form_update.html"
    fields = ["title", "content"]
    success_url = reverse_lazy("home")

    def get_form(self, form_class=None): 
        form = super().get_form(form_class)  # Correcta llamada a super()
        form.fields["title"].widget = forms.TextInput(attrs={"class": "form-control mb-2", 'placeholder': "Título"})
        form.fields["content"].widget = forms.Textarea(attrs={"class": "form-control mb-2", 'placeholder': "Contenido"})
        return form