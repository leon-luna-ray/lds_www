from django.db import models

from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel

class HomePage(Page):
    # pass
    # database fields
    # hero_image = models.ForeignKey(
    #     'wagtailimages.Image',
    #     null=True,
    #     blank=True,
    #     on_delete=models.SET_NULL,
    #     related_name='+'
    # )
    intro_text = RichTextField(null=True)

    # # config
    # max_count = 1
    # subpage_types = []
    content_panels = Page.content_panels + [
        FieldPanel('intro_text'),
        # FieldPanel('body'),
    ]
