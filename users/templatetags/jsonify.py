from django import template
import json

register = template.Library()

@register.filter
def jsonify(data):
    return json.dumps(data)
