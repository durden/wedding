from django import template
from wedding.wedding_app.models import *

register = template.Library()

class UpdatesNode(template.Node):
    def render(self, context):
        max_title = 20
        blogs = Blog.objects.all().order_by("-updated")[:3]
        pages = Page.objects.all().order_by("-updated")[:2]

        html = "<ul id='latest'>"

        for blog in blogs:
            extra_str = ""
            date = blog.updated.strftime("%Y/%m/%d")

            if len(blog.title) > max_title:
                extra_str = "..."

            html = html + '<li><a href="/blog/%s">%s</a> %s<span class="smalltxt"> (%s)</span></li>' % \
                            (date, blog.title[:max_title], extra_str, date)

        # FIXME: Bad to hardcode these names here b/c now there are dependencies
        #        here, views, and urls
        for page in pages:
            date = page.updated.strftime("%Y/%m/%d")

            if page.name == "Our Story":
                link = "story"
            elif page.name == "Gift Registry":
                link = "gifts"
            else:
                link = "home"

            html = html + '<li><a href="/%s">%s</a><span class="smalltxt"> (%s)</span></li>' % (link, page.name[:max_title], date) 
        html = html + "</ul>"
        return html

@register.tag(name="updates")
def find_updates(parser, token):
    return UpdatesNode()
