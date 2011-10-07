from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
                       
    (r'^quecomer/$', 'quecomer.views.index'),
    (r'^quecomer/platos/(?P<idplato>\d+)$', 'quecomer.views.detalle_plato'),
    (r'^quecomer/platos/(?P<idplato>\d+)/edit$', 'quecomer.views.edit_plato'),

    # Example:
    # (r'^quecomer/', include('quecomer.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
