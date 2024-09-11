from django.urls import path
from . import views

urlpatterns = [
    # TODO URLs contacto.
    path("contact_messages/", views.ContactListView.as_view(), name="contact-messages"),
    path("contact_detail/<int:pk>/", views.ContactDetailView.as_view(), name="contact-detail"),
    path("contact_delete/<int:pk>/", views.ContactDeleteView.as_view(), name="contact-delete"),
    # TODO URLs citas.
    path("appointment_messages/", views.AppointmentListView.as_view(), name="appointment-messages"),
    path("appointment_detail/<int:pk>/", views.AppointmentDetailView.as_view(), name="appointment-detail"),
    path("appointment_delete/<int:pk>/", views.AppointmentDeleteView.as_view(), name="appointment-delete"),
    # TODO URLs Status 200
    path("status_200/", views.Status200TemplateView.as_view(), name="status-200")
]
