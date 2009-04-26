from django import template

import random

register = template.Library()

class Image:
    def __init__(self, name, width, height):
        self.name = name
        self.width = width
        self.height = height

images = [
    Image('lukenatalie1.jpg', 208, 275),
    Image('lukenatalie2.jpg', 308, 232),
    Image('lukenatalie3.jpg', 308, 233),
    Image('lukenatalie4.jpg', 308, 308),
    Image('lukenatalie5.jpg', 308, 233),
    Image('lukenatalie6.jpg', 308, 233),
    Image('lukenatalie7.jpg', 308, 233),
    Image('lukenatalie8.jpg', 308, 233),
    Image('lukenatalie9.jpg', 208, 275),
    Image('lukenatalie10.jpg', 308, 232),
    Image('lukenatalie11.jpg', 308, 232),
]

class ImagesNode(template.Node):
    def render(self, context):
        img = random.choice(images)
        html = '<img id="page_img" src="/wmedia/img/%s" width="%d" height="%d" alt="Luke and Natalie"/>' % (img.name, img.width, img.height)
        return html

@register.tag(name="random_image")
def get_image(parser, token):
    return ImagesNode()

