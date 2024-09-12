from django.shortcuts import render
from django.views.generic import DetailView
from .models import AboutInfo

# Create your views here.

class AboutDetailView(DetailView):
    template_name = "about_us/about_detail.html"
    model = AboutInfo
    context_object_name = "about"
