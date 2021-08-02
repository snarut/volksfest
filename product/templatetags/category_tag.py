from django import template
from wagtail.core.models import Site
from product.models import Category

register = template.Library()

@register.simple_tag
def get_all_categories():
    return Category.objects.all()

@register.simple_tag(takes_context=True)
def get_products_by_category(context, category):
    current_site = Site.find_for_request(context['request'])
    return category.get_usage().in_site(current_site)
