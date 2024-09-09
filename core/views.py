from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class HomeTemplateView(TemplateView):
    template_name = "core/index.html"

class AboutTemplateView(TemplateView):
    template_name = "core/about.html"

class ContactTemplateView(TemplateView):
    template_name = "core/contact.html"

class DoctorTemplateView(TemplateView):
    template_name = "core/doctor.html"

class TestimonialTemplateView(TemplateView):
    template_name = "core/testimonial.html"

class TreatmentTemplateView(TemplateView):
    template_name = "core/treatment.html"