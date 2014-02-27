from django.conf.urls import patterns, include, url

from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('sample_apis.views',
                       url(r'^snippets/$', 'snippet_list'),
                       url(r'^snippets/(?P<pk>[0-9]+)/$', 'snippet_detail'),
                       url(r'^images', 'sample_image_list'),
)