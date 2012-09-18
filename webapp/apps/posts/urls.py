#Django
from django.conf.urls import patterns, url

urlpatterns = patterns('webapp.apps.posts.views',
    url(r'^$', 'list', name='blog'),
    url(r'^(?P<page_id>\d+)/$', 'list', name="post-list"),
    url(r'^posts/(?P<post_id>\d+)/$', 'detail', name="post-detail"),
)
