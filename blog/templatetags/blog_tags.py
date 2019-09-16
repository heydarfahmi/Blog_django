from django import template
from django.db.models import Count

from ..models import Post

register = template.Library()


@register.simple_tag
def total_posts():
    return Post.published.count()


@register.inclusion_tag('blog/latest_post.html')
def show_latest_posts(count=5):
    latest_posts = Post.published.order_by('-created')[:count]
    return {'latest_posts': latest_posts}
@register.simple_tag
def get_most_commented_post(count=5):
    return Post.published.annotate(count=Count('comments')).order_by('-count')[:count]