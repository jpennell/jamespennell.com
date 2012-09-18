#Django
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

#Annoying
from annoying.decorators import render_to

#Webapp
from models import Post


@render_to('posts/list.html')
def list(request, page_id=1):
    paginator = Paginator(Post.objects.all(), 5)
    try:
        posts = paginator.page(page_id)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return {'posts': posts}


@render_to('posts/detail.html')
def detail(request, post_id):
    return {'post': get_object_or_404(Post, pk=post_id)}
