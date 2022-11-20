from django.db import models

from wagtail.admin.panels import FieldPanel

from apps.base.models.pages import BasePage


class GalleryPostPage(BasePage):

    content_panels = BasePage.content_panels
    template = 'gallery/gallery_post_page.html'
    parent_page_types = ['gallery.GalleryLandingPage']

class GalleryLandingPage(BasePage):

    content_panels = BasePage.content_panels
    template = 'gallery/gallery_landing_page.html'
    subpage_types = ['gallery.GalleryPostPage']
    parent_page_types = ['services.ServicesLandingPage']
