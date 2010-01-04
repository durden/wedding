"""Image template tags"""

from django import template

import random

register = template.Library()


class Image:
    """Container class for image"""

    def __init__(self, name, width, height):
        self.name = name
        self.width = width
        self.height = height

IMAGES = [
    # Trying to order by size, not number
    Image('lukenatalie1.jpg', 208, 275),
    Image('lukenatalie9.jpg', 208, 275),
    Image('lukenatalie4.jpg', 308, 308),
    Image('lukenatalie2.jpg', 308, 232),
    Image('lukenatalie3.jpg', 308, 233),
    Image('lukenatalie5.jpg', 308, 233),
    Image('lukenatalie6.jpg', 308, 233),
    Image('lukenatalie7.jpg', 308, 233),
    #Image('lukenatalie8.jpg', 308, 233),
    Image('lukenatalie10.jpg', 308, 232),
    Image('lukenatalie11.jpg', 308, 232),
    Image('lukenatalie12.jpg', 308, 232),
]


class RandomImageNode(template.Node):
    """Node to handle random_image tag"""

    def render(self, context):
        """Find random image and return html to display it"""

        img = random.choice(IMAGES)
        html = '<img id="page_img" src="/wmedia/img/%s" width="%d" height="%d" alt="Luke and Natalie">' % (img.name, img.width, img.height)
        return html


@register.tag(name="random_image")
def get_random_image(parser, token):
    """random_image template tag"""
    return RandomImageNode()


class AllImagesNode(template.Node):
    """Node to handle all_images template tag"""

    def render(self, context):
        """Find all images and return html to display them as a list"""

        cnt = 0
        html = '<ul id="images">'
        for img in IMAGES:
            img_tag = '<img src="/wmedia/img/%s" width="%d" height="%d" alt="Luke and Natalie">' % (img.name, img.width, img.height)

            if not cnt:
                html = html + "<li>" + img_tag
            else:
                html = html + img_tag + "</li>"

            cnt = not cnt
        html = html + "</ul>"
        return html


@register.tag(name="all_images")
def get_all_images(parser, token):
    """all_images template tag"""
    return AllImagesNode()
