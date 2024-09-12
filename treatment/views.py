from django.shortcuts import render
from django.views.generic import DetailView
from .models import Treatment

# Create your views here.

class TreatmentDetailView(DetailView):
    template_name = "treatment/treatment_detail.html"
    model = Treatment
    context_object_name = "treatment"
