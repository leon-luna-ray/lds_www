from django.db import models

from wagtail.models import Page
from wagtail.fields import RichTextField, StreamField
from wagtail.admin.panels import FieldPanel
from wagtail.images.blocks import ImageChooserBlock


class HomePage(Page):
    # pass
    banner_carousel = StreamField(
        [
            ('carousel_item', ImageChooserBlock(
                required=True)
            ),
        ],
        block_counts={
            'carousel_item': {'min_num': 2, 'max_num': 5}
        },
        blank=False,
        null=True,
    )

    intro_text = RichTextField(null=True)

    # config
    max_count = 1
    subpage_types = []
    content_panels = Page.content_panels + [
        FieldPanel('intro_text'),
        FieldPanel('banner_carousel'),
    ]
