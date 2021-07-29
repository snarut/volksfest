from django.db import models
from django.db.models.fields.related import ForeignKey
from django import forms

from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel, PageChooserPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from modelcluster.fields import ParentalKey, ParentalManyToManyField


class HomePage(Page):
    hero_title = models.CharField(max_length=100, default='Hello World')
    hero_text = models.CharField(max_length=300, default='')
    hero_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
    )
    featureds = ParentalManyToManyField(
        'product.ProductPage',
        blank=True,
    )

    content_panels = Page.content_panels + [
        FieldPanel("hero_title"),
        FieldPanel("hero_text"),
        ImageChooserPanel("hero_image"),
        FieldPanel("featureds", widget=forms.CheckboxSelectMultiple),
    ]

    parent_page_types = []
    subpage_types = ['product.ProductsListPage']
