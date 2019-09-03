from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from taggit.models import Tag

from blog.models import Post


def list_of_posts(request, tag_slug=None):
    post_list = Post.published.all()
    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        post_list = Post.published.filter(tags__in=[tag])
    paginator = Paginator(post_list, 4)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(paginator.num_pages)
    except EmptyPage:
        posts = paginator.page(1)

    return render(request, './blog/listed_post.html', context={'posts': posts, tag: tag})
# Create your views here.
