from django.db import models
from wagtail.fields import StreamField
from wagtail.admin.panels import FieldPanel
from apps.base.models.pages import BasePageWithOptions
from apps.base.models.blocks import BodySectionBlock


# Services
class ServicesLandingPage(BasePageWithOptions):
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
    template = 'services/services_landing.html'
    # subpage_types = ['gallery.GalleryLandingPage']
