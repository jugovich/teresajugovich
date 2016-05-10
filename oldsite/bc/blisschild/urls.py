from django.conf.urls import include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from django.conf.urls import patterns

urlpatterns = patterns('blisschild.views',
     (r'^admin/', include(admin.site.urls)),
     url('^$', 'landing', name="home"),
)

urlpatterns += staticfiles_urlpatterns()