from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'extras_example.views.home', name='home'),
    # url(r'^extras_example/', include('extras_example.foo.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
