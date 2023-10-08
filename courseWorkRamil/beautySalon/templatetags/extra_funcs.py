from django import template

register = template.Library()

@register.simple_tag()
def all_specs(master):
    return master.specialization.all()