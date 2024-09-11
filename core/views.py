from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView
from appointments.forms import Appointment_form
from appointments.models import Appointment

# Create your views here.
class HomeTemplateView(TemplateView):
    template_name = "core/index.html"

    def get_context_data(self, **kwargs): # -> This logic allows sent instances-model the model DeppartmentAppointment through that form
        context = super().get_context_data(**kwargs)
        context['form'] = Appointment_form()
        return context

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login') 

        form = Appointment_form(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.user = request.user
            appointment.save()
            return redirect('status-200')
        return self.get(request, *args, **kwargs, form=form)
    
class AboutTemplateView(TemplateView):
    template_name = "core/about.html"
class DoctorTemplateView(TemplateView):
    template_name = "core/doctor.html"

class TestimonialTemplateView(TemplateView):
    template_name = "core/testimonial.html"

class TreatmentTemplateView(TemplateView):
    template_name = "core/treatment.html"