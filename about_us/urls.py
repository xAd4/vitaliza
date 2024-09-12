from django.urls import path
from . import views

urlpatterns = [
    path("<int:pk>/", views.AboutDetailView.as_view(), name="about-detail"),
    path("update/<int:pk>/", views.AboutUpdateView.as_view(), name="about-update"),
]
