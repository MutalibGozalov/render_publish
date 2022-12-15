from django import template
from datetime import timedelta

register = template.Library()


@register.filter
def to_str(value):
    s = str(value)
    return s[0:4]

@register.filter
def to_hm(value):
    s = str(value)
    hm = s[0:1]+"h "+s[2:4]+"min"
    return hm

@register.filter
def outcome(assignment):
    outcome = assignment.service.prize + assignment.tip
    return outcome