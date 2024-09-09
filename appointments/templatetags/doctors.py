from django import template
from doctors.models import Doctor

register = template.Library()

@register.simple_tag
def get_doctor():
    doctor = Doctor.objects.all()
    return doctor