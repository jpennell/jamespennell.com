#Django
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic.simple import redirect_to
from django.conf import settings

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('',
    url(r'^$', redirect_to, {'url': '/posts/'}),
    url(r'^posts/', include('webapp.apps.posts.urls')),
)

if settings.DEBUG:
    urlpatterns += patterns('django.contrib.staticfiles.views',
        url(r'^static/(?P<path>.*)$', 'serve'),
    )
