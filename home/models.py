from django.db import models

from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel


class HomePage(Page):
    hero_title = models.CharField(max_length=100, default='Hello World')
    hero_text = models.CharField(max_length=300, default='')
    hero_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
    )

    content_panels = Page.content_panels + [
        FieldPanel("hero_title"),
        FieldPanel("hero_text"),
        ImageChooserPanel("hero_image"),
    ]
