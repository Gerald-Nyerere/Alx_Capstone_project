from django import template

register = template.Library()

@register.filter
def dict_get(d, key):
    """Return value of dictionary key"""
    if isinstance(d, dict):
        return d.get(key)
    return None
