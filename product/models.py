from django.db import models
from modelcluster.fields import ParentalKey

from wagtail.core.models import Orderable, Page
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.snippets.models import register_snippet
from wagtail.snippets.edit_handlers import SnippetChooserPanel

from django import template

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
    product_price = models.CharField(max_length=100, default='')
    product_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )
    product_category = models.ForeignKey(
        'Category',
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )

    content_panels = Page.content_panels + [
        FieldPanel("product_title"),
        FieldPanel("product_description"),
        FieldPanel("product_price"),
        ImageChooserPanel("product_image"),
        InlinePanel('more_product_image', label="More Image", min_num=0, max_num=4),
        SnippetChooserPanel("product_category"),
    ]

    parent_page_types = ['product.ProductsListPage']
    subpage_types = []

    def __str__(self):
        return self.product_title
    
    

@register_snippet
class Category(models.Model):
    text = models.CharField(max_length=50)

    panels = [
        FieldPanel('text'),
    ]

    def __str__(self):
        return self.text

class MoreProductImage(Orderable):
    page = ParentalKey(ProductPage, on_delete=models.CASCADE, related_name='more_product_image')
    image = models.ForeignKey(
        'wagtailimages.Image', 
        on_delete=models.CASCADE,
        related_name='+'
    )

    panels = [
        ImageChooserPanel('image'),
    ]