from django.db import models

from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel
from wagtail.contrib.settings.models import BaseSetting, register_setting

# Create your models here.


@register_setting
class ContactInfo(BaseSetting):
    """ Org contact information """
    company_name = models.CharField(blank=True, null=True, max_length=255)
    admin_name = models.CharField(blank=True, null=True, max_length=255)
    phone = models.CharField(blank=True, null=True, max_length=255)
    email = models.CharField(blank=True, null=True, max_length=255)
    website = models.URLField(blank=True, null=True)
    street = models.CharField(blank=True, null=True, max_length=255)
    colonia = models.CharField(blank=True, null=True, max_length=255)
    city = models.CharField(blank=True, null=True, max_length=255)
    state = models.CharField(blank=True, null=True, max_length=255)
    postal_code = models.CharField(blank=True, null=True, max_length=255)
    country = models.CharField(blank=True, null=True, max_length=255)
    facebook = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)

    panels = [
        MultiFieldPanel([
            FieldPanel('company_name'),
            FieldPanel('admin_name'),
            FieldPanel('phone'),
            FieldPanel('email'),
            FieldPanel('website'),
            MultiFieldPanel([
                FieldPanel('street'),
                FieldPanel('colonia'),
                FieldPanel('city'),
                FieldPanel('state'),
                FieldPanel('postal_code'),
                FieldPanel('country'),
            ], heading="Address")
        ], heading='Contact'),
        MultiFieldPanel([
            FieldPanel('facebook'),
            FieldPanel('instagram'),
        ], heading='Social Media'),
    ]
