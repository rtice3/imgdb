from django import template

register = template.Library()


@register.filter
def get_path_resolve(obj):
    return obj.get_path()
