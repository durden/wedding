"""Wedding date countdown template tag"""

from django import template

from datetime import date

register = template.Library()


class CountdownNode(template.Node):
    """Node to handle countdown tag"""

    def render(self, context):
        """Compute # days until wedding date and return as phrase"""

        wedding_date = date(2009, 10, 17)
        diff = wedding_date - date.today()
        return "%s days until wedding" % (diff.days)


@register.tag(name="countdown")
def countdown(parser, token):
    """Countdown tag"""
    return CountdownNode()
