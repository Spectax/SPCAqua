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
    url(r'^add/purchasebill/$', 'spcaqua.views.add_purchase_bill', name='addpurchasebill'),
    url(r'^add/companybill/$', 'spcaqua.views.add_company_bill', name='addcompanybill'),
    url(r'^add/lot/$', 'spcaqua.views.add_lot', name='addlot'),
    url(r'^search/companybill/$', 'spcaqua.views.search_company_bill', name='searchcompanybill'),
    url(r'^search/purchasebill/$', 'spcaqua.views.search_purchase_bill', name='searchpurchasebill'),
    url(r'^search/lot/$', 'spcaqua.views.search_lot', name='searchlot'),
    url(r'^print/purchasebill/$', 'spcaqua.views.print_purchase_bill', name='printpurchasebill'),
    url(r'^print/companybill/$', 'spcaqua.views.print_company_bill', name='printcompanybill'),
)
