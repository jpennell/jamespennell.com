#Django
from django.conf.urls import patterns, url

urlpatterns = patterns('webapp.apps.posts.views',
    url(r'^$', 'list', name='post-list'),
    url(r'^(?P<post_id>\d+)/$', 'detail', name="post-detail"),
)
