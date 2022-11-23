from django.db import models
from wagtail.fields import StreamField
from wagtail.admin.panels import FieldPanel
from wagtail.images.blocks import ImageChooserBlock
from apps.base.models.pages import BasePageWithOptions


# Create your models here.
class ImageGalleryPage(BasePageWithOptions):
    images = StreamField([
        ('image', ImageChooserBlock())
    ],
        blank=False,
        null=True,
        use_json_field=False,
    )
    content_panels = BasePageWithOptions.intro_with_image_panel + [
        FieldPanel('images')
    ]

    template = 'image_gallery/image_gallery.html'
    subpage_types = []
