from django.db import models
from apps.base.models.pages import BasePageWithOptions

# Services
class ServicesLandingPage(BasePageWithOptions):

    content_panels = BasePageWithOptions.intro_with_image_panel +[]

    # config
    max_count = 1
    template = 'services/services_landing.html'
