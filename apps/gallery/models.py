from django.db import models
from wagtail.fields import StreamField
from wagtail.admin.panels import FieldPanel
from wagtail.images.blocks import ImageChooserBlock
from apps.base.models.pages import BasePageWithOptions

class ImageGallery(BasePageWithOptions):
    images = StreamField([
        ('image', ImageChooserBlock())
    ],
        blank=False,
        null=True,
        max_num=1,
        use_json_field=False,
    )

    content_panels = BasePageWithOptions.intro_with_image_panel + [
        FieldPanel('images'),
    ]

    # config
    max_count = 1
    template = 'image_gallery/image_gallery.html'
    # subpage_types = ['gallery.GalleryLandingPage']
