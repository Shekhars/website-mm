import os

from django import template


register = template.Library()

@register.filter
def filename(value):
    return os.path.basename(value.form16.name)
