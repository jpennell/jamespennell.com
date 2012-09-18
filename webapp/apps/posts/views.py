#Django
from django.shortcuts import get_object_or_404

#Annoying
from annoying.decorators import render_to

#Webapp
from models import Post


@render_to('posts/list.html')
def list(request):
    return {'posts': Post.objects.all()}


@render_to('posts/detail.html')
def detail(request, post_id):
    return {'post': get_object_or_404(Post, pk=post_id)}
