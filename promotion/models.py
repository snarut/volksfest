from django.db import models
from modelcluster.fields import ParentalKey

from wagtail.core.fields import RichTextField
from wagtail.core.models import Orderable, Page
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel
from wagtail.images.edit_handlers import ImageChooserPanel

# Create your models here.
class PromotionPage(Page):
    promotion_header = models.CharField(max_length=100, default='Promotion')
    promotion_short_text = models.CharField(max_length=300, default='')
    promotion_text = RichTextField(features=['h4', 'h5', 'bold', 'italic'])
    promotion_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
    )

    content_panels = Page.content_panels + [
        FieldPanel('promotion_header'),
        FieldPanel('promotion_short_text'),
        FieldPanel('promotion_text'),
        ImageChooserPanel('promotion_image'),
        InlinePanel('more_promotion_image', label="More Image", min_num=0, max_num=4),
    ]

    parent_page_types = ['promotion.PromotionsListPage']
    subpage_types = []

class MorePromotionImage(Orderable):
    page = ParentalKey(PromotionPage, on_delete=models.CASCADE, related_name='more_promotion_image')
    image = models.ForeignKey(
        'wagtailimages.Image', 
        on_delete=models.CASCADE,
        related_name='+'
    )

    panels = [
        ImageChooserPanel('image'),
    ]

class PromotionsListPage(Page):
    hero_text = models.CharField(max_length=100, default='Promotions')
    hero_subtext = models.CharField(max_length=300, default='', blank=True)
    hero_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
    )

    content_panels = Page.content_panels + [
        FieldPanel('hero_text'),
        FieldPanel('hero_subtext'),
        ImageChooserPanel('hero_image')
    ]

    parent_page_type = ['home.HomePage']
    subpage_types = ['promotion.PromotionPage']