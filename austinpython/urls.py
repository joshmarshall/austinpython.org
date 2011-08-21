from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'austinpython.views.home', name='home'),
    # url(r'^austinpython/', include('austinpython.foo.urls')),
    url(r'^register/austinpython$',
        'austinpython.registration.views.register_austinpython_get'),
    url(r'^register/austinpython/submit',
        'austinpython.registration.views.register_austinpython_post')

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
