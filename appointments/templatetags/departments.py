from django import template
from departments.models  import Deparment

register = template.Library()

@register.simple_tag
def get_department():
    department = Deparment.objects.all()
    return department