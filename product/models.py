from django.db import models

from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel

class ProductsListPage(Page):
    hero_title = models.CharField(max_length=100, default='Our Products')
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

    parent_page_types = ['home.HomePage']
    subpage_types = ['product.ProductPage']


class ProductPage(Page):
    product_title = models.CharField(max_length=100, default='Product Name')
    product_description = models.CharField(max_length=500, default='')
    product_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )

    content_panels = Page.content_panels + [
        FieldPanel("product_title"),
        FieldPanel("product_description"),
        ImageChooserPanel("product_image"),
    ]

    parent_page_types = ['product.ProductsListPage']
    subpage_types = []