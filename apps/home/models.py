from django.db import models
from wagtail.models import Page
from wagtail.fields import RichTextField, StreamField
from wagtail.admin.panels import FieldPanel
from wagtail.images.blocks import ImageChooserBlock

from apps.base.models.pages import BasePage, BasePageWithOptions


class HomePage(BasePage):
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


    # Link Block to other pages (block (image + text + page or url))
    # Annoucments/promotions (block)
    # Featured works (orderable)

    intro_text = RichTextField(null=True)

    # config
    max_count = 1
    subpage_types = ['home.AboutPage', 'home.ServicesLandingPage']
    content_panels = Page.content_panels + [
        FieldPanel('intro_text'),
        FieldPanel('banner_carousel'),
    ]

# About
class AboutPage(BasePageWithOptions):

    content_panels = BasePageWithOptions.intro_with_image_panel +[]

    # config
    max_count = 1
    template = 'home/about.html'

# Services
class ServicesLandingPage(BasePageWithOptions):

    content_panels = BasePageWithOptions.intro_with_image_panel +[]

    # config
    max_count = 1
    template = 'home/services.html'
