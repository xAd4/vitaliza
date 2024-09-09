from django.urls import path
from . import views

urlpatterns = [
    path("", views.HomeTemplateView.as_view(), name="home"),
    path("about/", views.AboutTemplateView.as_view(), name="about"),
    path("doctor/", views.DoctorTemplateView.as_view(), name="doctor"),
    path("testimonial/", views.TestimonialTemplateView.as_view(), name="testimonial"),
    path("treatment/", views.TreatmentTemplateView.as_view(), name="treatment"),
]
