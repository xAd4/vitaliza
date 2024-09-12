from django.urls import path
from . import views

urlpatterns = [
    path("<int:pk>/", views.TreatmentDetailView.as_view(), name="treatment-detail"),
    path("update/<int:pk>/", views.TreatmentUpdateView.as_view(), name="treatment-update"),
]
