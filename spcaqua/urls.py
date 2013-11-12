from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'spcaqua.views.home', name='home'),
    # url(r'^spcaqua/', include('spcaqua.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^account/login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^account/logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}, name='logout'),
    url(r'^menu/$', 'spcaqua.views.menu', name='menu'),
    url(r'^search/$', 'spcaqua.views.search', name='search'),
    url(r'^purchasebill/$', 'spcaqua.views.purchasebill', name='purchasebill'),
    url(r'^companybill/$', 'spcaqua.views.companybill', name='companybill'),
    url(r'^printpurchasebill/$', 'spcaqua.views.printpurchasebill', name='printpurchasebill'),
    url(r'^printcompanybill/$', 'spcaqua.views.printcompanybill', name='printcompanybill'),
)
