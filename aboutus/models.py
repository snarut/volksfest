from django.db import models
from modelcluster.fields import ParentalKey

from wagtail.core.models import Orderable, Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel, RichTextFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.snippets.edit_handlers import SnippetChooserPanel
from wagtail.snippets.models import register_snippet

class AboutusPage(Page):
    hero_title = models.CharField(max_length=100, default='เกี่ยวกับเรา')
    hero_text = RichTextField(features=['h2', 'h3', 'bold', 'italic', 'link', 'image'])
    hero_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name='+',
    )
    first_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name='first_image',
    )
    second_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name='second_image',
    )
    third_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name='third_image',
    )

    content_panels = Page.content_panels + [
        FieldPanel("hero_title"),
        FieldPanel("hero_text", classname="full"),
        ImageChooserPanel("hero_image"),
        ImageChooserPanel("first_image"),
        ImageChooserPanel("second_image"),
        ImageChooserPanel("third_image"),
        InlinePanel("reviews", label="Review"),
    ]

    parent_page_types = ['home.HomePage']

@register_snippet
class Review(models.Model):
    review_text = RichTextField(features=['bold', 'italic'])
    review_by = models.CharField(max_length=100)
    
    panels = [
        FieldPanel('review_text'),
        FieldPanel('review_by'),
    ]

    def __str__(self):
        return self.review_by

class ReviewsOrderable(Orderable):
    page = ParentalKey(AboutusPage, related_name='reviews')

    review = models.ForeignKey(
        "aboutus.Review",
        on_delete=models.CASCADE,
    )

    panels = [
        SnippetChooserPanel("review"),
    ]