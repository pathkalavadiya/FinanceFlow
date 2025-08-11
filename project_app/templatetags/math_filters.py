from django import template
from decimal import Decimal

register = template.Library()

@register.filter
def abs_value(value):
    """Return the absolute value of a number"""
    try:
        if isinstance(value, (int, float, Decimal)):
            return abs(value)
        return value
    except (TypeError, ValueError):
        return value

@register.filter
def multiply(value, arg):
    """Multiply the value by the argument"""
    try:
        return float(value) * float(arg)
    except (ValueError, TypeError):
        return value

@register.filter
def divide(value, arg):
    """Divide the value by the argument"""
    try:
        return float(value) / float(arg)
    except (ValueError, TypeError, ZeroDivisionError):
        return value

@register.filter
def dict_get(mapping, key):
    """Safely get a value from a dict-like object by key"""
    try:
        return mapping.get(key, '')
    except Exception:
        return ''