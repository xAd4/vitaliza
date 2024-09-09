from django import template
from appointments.forms import Appointment_form

register = template.Library()

@register.inclusion_tag("appointments/forms/appointment_form.html", takes_context=True)
def appointment_form(context):
    request = context["request"]
    if request.user.is_authenticated:
        form = Appointment_form()
        return {"form":form}
    else:
        return {"form": None}