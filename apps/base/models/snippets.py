from django.db import models

from wagtail.admin.panels import FieldPanel
from wagtail.snippets.models import register_snippet

# ...


@register_snippet
class Employee(models.Model):
    name = models.CharField(max_length=255)
    position = models.CharField(max_length=255, blank=True, null=True)
    intro = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)

    panels = [
        FieldPanel('name'),
        FieldPanel('position'),
        FieldPanel('intro'),
        FieldPanel('email'),
    ]

    def __str__(self):
        return self.text
