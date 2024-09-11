from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView
from .forms import Contact_form
from .models import Contact

# Create your views here.

class ContactFormView(FormView):
    template_name = "contact/contact.html"
    form_class = Contact_form
    success_url = reverse_lazy("status-200")

    def form_valid(self, form):
        # Crear una instancia del modelo Contact usando los datos del formulario
        Contact.objects.create(
            full_name=form.cleaned_data['full_name'],
            email=form.cleaned_data['email'],
            phone_number=form.cleaned_data['phone_number'],
            message=form.cleaned_data['message']
        )
        return super().form_valid(form)


