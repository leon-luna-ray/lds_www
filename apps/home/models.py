from django.db import models

from wagtail.models import Page
from wagtail.fields import StreamField
from wagtail.admin.panels import FieldPanel
from wagtail.images.blocks import ImageChooserBlock

from apps.base.models.pages import BasePage, BasePageWithOptions
from apps.base.models.blocks import BodySectionBlock


class HomePage(BasePage):

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
        use_json_field=False,
    )

    content = StreamField([
        ('sections', BodySectionBlock())
    ],
        blank=False,
        null=True,
        max_num=1,
        use_json_field=False,
    )

    # Link Block to other pages (block (image + text + page or url))
    # Annoucments/promotions (block)
    # Featured works (orderable)

    # config
    max_count = 1
    subpage_types = ['home.AboutPage', 'home.GenericPage','services.ServicesLandingPage']
    content_panels = BasePage.content_panels + [
        FieldPanel('banner_carousel'),
        FieldPanel('content'),
    ]


# About
class AboutPage(BasePageWithOptions):
    content = StreamField([
        ('sections', BodySectionBlock())
    ],
        blank=False,
        null=True,
        max_num=1,
        use_json_field=False,
    )

    content_panels = BasePageWithOptions.intro_with_image_panel + [
        FieldPanel('content'),
    ]


    # config
    max_count = 1
    template = 'home/about.html'

# Generic
class GenericPage(BasePageWithOptions):
    content = StreamField([
        ('sections', BodySectionBlock())
    ],
        blank=False,
        null=True,
        max_num=1,
        use_json_field=False,
    )

    content_panels = BasePageWithOptions.intro_with_image_panel + [
        FieldPanel('content'),
    ]


    # config
    parent_page_types = ['home.HomePage']
    template = 'home/generic.html'
