from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^events/', include('events.urls')),
    url(r'^friends/', include('socialgraph.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
