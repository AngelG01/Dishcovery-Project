from django import template

register = template.Library()


@register.filter
def to_range(value):
    """Generate a range from 1 to the specified value (inclusive)."""
    return range(1, value + 1)
