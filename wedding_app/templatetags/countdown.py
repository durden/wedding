from django import template

from datetime import date

register = template.Library()

class CountdownNode(template.Node):
    def render(self, context):
        wedding_date = date(2009, 10, 17)
        diff = wedding_date - date.today()
        return "%s days until wedding" % (diff.days)

@register.tag(name="countdown")
def countdown(parser, token):
    return CountdownNode()

