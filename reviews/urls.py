from django.conf.urls.defaults import *
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(",
    # Examples:
    (r'^$', 'reviewapp.reviews.views.homepage', name='homepage'),
    #(r'^reviewapp/$', include('reviewapp.reviews.views.rating'),
    #(r'^reviews/(?P<rating>[-\w]+)/$',reviewapp.reviews.views.rating'),
    # Uncomment the admin/doc line below to enable admin documentation:
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
)
