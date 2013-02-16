from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin

from myproject.views import testview

admin.autodiscover()


urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', testview),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
