from django import template
from contact.forms import Contact_form

register = template.Library()

@register.inclusion_tag("contact/forms/contact_form.html", takes_context=True)
def contact_form(context):
    request = context["request"]
    if request.user.is_authenticated:
        form = Contact_form()
        return {"form":form}
    else:
        return {"form": None}