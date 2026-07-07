import os
from django import template
from django.templatetags.static import static
from django.conf import settings

register = template.Library()

@register.filter
def image_url(value):
    if not value:
        return static('app/images/salta.png')
    if value.startswith(('http://', 'https://')):
        return value
    return static('app/images/' + value)

@register.simple_tag
def available_images():
    images_dir = settings.BASE_DIR / 'app' / 'static' / 'app' / 'images'
    files = []
    if images_dir.exists():
        for f in sorted(images_dir.iterdir()):
            if f.suffix.lower() in ('.png', '.jpg', '.jpeg', '.gif', '.webp'):
                files.append(f.name)
    return files
