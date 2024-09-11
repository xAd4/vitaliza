from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.admin.views.decorators import staff_member_required
from django.views.generic import ListView, DetailView, TemplateView, DeleteView
from contact.models import Contact
from appointments.models import Appointment

# Create your views here.

# TODO Instancias de contacto.
@method_decorator(staff_member_required, name="dispatch")
class ContactListView(ListView):
    template_name = "developer_options/contact_message.html"
    model = Contact

@method_decorator(staff_member_required, name="dispatch")
class ContactDetailView(DetailView):
    template_name = "developer_options/contact_detail.html"
    model = Contact

@method_decorator(staff_member_required, name="dispatch")
class ContactDeleteView(DeleteView):
    template_name = "developer_options/forms/confirm_delete.html"
    model = Contact
    success_url = reverse_lazy("contact-messages")
    
    
# TODO Instancias de contacto.
@method_decorator(staff_member_required, name="dispatch")
class AppointmentListView(ListView):
    template_name = "developer_options/appointment_message.html"
    model = Appointment

@method_decorator(staff_member_required, name="dispatch")
class AppointmentDetailView(DetailView):
    template_name = "developer_options/appointment_detail.html"
    model = Appointment

@method_decorator(staff_member_required, name="dispatch")
class AppointmentDeleteView(DeleteView):
    template_name = "developer_options/forms/confirm_delete.html"
    model = Appointment
    success_url = reverse_lazy("appointment-messages")

# TODO Template Status 200
class Status200TemplateView(TemplateView):
    template_name = "developer_options/models/status_200.html"
