from django import template


register = template.Library()


@register.filter(name='times')
def total_range(number):
    return range(number)
