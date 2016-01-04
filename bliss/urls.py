from django.conf.urls import include, url
from dolove import views
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
admin.autodiscover()


urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'about$', views.about, name='about'),
    url(r'doula_description$', views.doula_description, name='doula_description'),
    url(r'doula_services$', views.doula_services, name='doula_services'),
    url(r'photo_gallery$', views.photo_gallery, name='photo_gallery'),
    url(r'photo_price$', views.photo_price, name='photo_price'),
    url(r'yoga_class$', views.yoga_class, name='yoga_class'),
    url(r'yoga_locations$', views.yoga_locations, name='yoga_locations'),
    url(r'yoga_schedule$', views.yoga_schedule, name='yoga_schedule'),
    url(r'yoga_price$', views.yoga_price, name='yoga_price'),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
