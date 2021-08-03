from django.db import models
from modelcluster.fields import ParentalKey

from wagtail.core.models import Page, Orderable
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel
from wagtail.images.edit_handlers import ImageChooserPanel


class GalleryPage(Page):
    gallery_text = models.CharField(max_length=100, default='Gallery')

    content_panels = Page.content_panels + [
        FieldPanel("gallery_text"),
        InlinePanel('gallery_images', label="Gallery Images"),
    ]

    parent_page_types = ['home.HomePage']
    subpage_types = []

class GalleryImage(Orderable):
    page = ParentalKey(GalleryPage, on_delete=models.CASCADE, related_name='gallery_images')
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
    )
    caption = models.CharField(blank=True, max_length=250)

    panels = [
        ImageChooserPanel('image'),
        FieldPanel('caption'),
    ]