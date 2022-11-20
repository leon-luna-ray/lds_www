from django.db import models

from wagtail.admin.panels import FieldPanel

from apps.base.models.pages import BasePageWithOptions


class GalleryPostPage(BasePageWithOptions):

    content_panels = BasePageWithOptions.intro_only_panel
    template = 'gallery/gallery_post_page.html'

class GalleryLandingPage(BasePageWithOptions):

    content_panels = BasePageWithOptions.intro_only_panel
    template = 'gallery/gallery_landing_page.html'
    subpage_types = ['gallery.GalleryPostPage']
