from django.template import Library

register=Library()

@register.filter(name='removeArgs')
def removeArgs(value, args):
    for char in args:
        value = value.replace(char, '')
    print(value)
    return value

@register.filter
def upper(value):
   return value.upper()