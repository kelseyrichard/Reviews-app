from django.conf.urls.defaults import *
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    (r'^$', 'reviewapp.reviews.views.homepage'),
    (r'^restaurant/(?P<restaurant>[-\w]+)/$','reviewapp.reviews.views.restaurant_detail'),
    (r'^review/(?P<rating_id>\d+)/$','reviewapp.reviews.views.rating_detail'),
    (r'^category/$','reviewapp.reviews.views.category'),
    (r'^category/(?P<category>[-\w]+)/$','reviewapp.reviews.views.category_detail'),
    (r'^types/$','reviewapp.reviews.views.restaurant_type'),
    (r'^types/(?P<resttype>[-\w]+)/$','reviewapp.reviews.views.restaurant_type_detail'),
    # Uncomment the admin/doc line below to enable admin documentation:
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
)

