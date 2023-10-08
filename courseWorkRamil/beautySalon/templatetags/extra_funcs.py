from django import template

from ..models import MasterRating

register = template.Library()

@register.simple_tag()
def get_all_specs(master):
    return master.specialization.all()


@register.simple_tag()
def get_rating(master):
    all_scores = MasterRating.objects.filter(evaluated_id=master.user.id)
    master_rating = 0 + sum([record.value for record in all_scores])
    return master_rating