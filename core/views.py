from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from contact.models import Contact
from contact.forms import Contact_form

# Create your views here.

class HomeTemplateView(TemplateView):
    template_name = "core/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = Contact_form()  # Añadir el formulario al contexto
        return context

    def post(self, request, *args, **kwargs):
        form = Contact_form(request.POST)
        if form.is_valid():
            # Crear una instancia del modelo Contact usando los datos del formulario
            Contact.objects.create(
                full_name=form.cleaned_data['full_name'],
                email=form.cleaned_data['email'],
                phone_number=form.cleaned_data['phone_number'],
                message=form.cleaned_data['message']
            )
            return redirect(reverse_lazy('home'))  # Redirigir a la URL de éxito
        else:
            # Si el formulario no es válido, renderizar de nuevo la página con los errores
            return self.render_to_response(self.get_context_data(form=form))

class AboutTemplateView(TemplateView):
    template_name = "core/about.html"
class DoctorTemplateView(TemplateView):
    template_name = "core/doctor.html"

class TestimonialTemplateView(TemplateView):
    template_name = "core/testimonial.html"

class TreatmentTemplateView(TemplateView):
    template_name = "core/treatment.html"