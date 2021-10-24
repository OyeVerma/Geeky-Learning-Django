create templatetags folder in app

in templatetags folder create '__init__.py' and 'filters.py' file

in filters.py file, write
"""
from django.template import Library
register=Library()

@register.filter(name='filter_name_to_be_used')
def filter(value, arg):
    **OPERATIONS**
    return value
"""

in html file, load filters.py as only {% load filters %}