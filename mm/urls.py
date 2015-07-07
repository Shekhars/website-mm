from django.conf.urls import include, url
from django.contrib import admin
from mudramantri import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    url(r'^$',views.index,name='home'),
    url(r'^index/$',views.index,name='register'),
    url(r'^admin/',include(admin.site.urls)),
    url(r'^confirm/(?P<activation_key>\w+)/', views.register_confirm),
     url(r'^login/$', views.loginUser,name='login'),
    url(r'^page-login.html/$', views.loginUser,name='login'),
    url(r'^logout', views.logoutUser,name='logout'),
    url(r'^itr/dashboard',views.dashboard,name='itrdash'),
    url(r'^itr/form16',views.itrFile,name='itrfile'),
    url(r'^itr/download',views.download,name='itrdownload'),
    url(r'^itr/checkout',views.checkout,name='itrcheckout'),
    url(r'^itr/BankDetails',views.bankDetails,name='bankDetails'),
    url(r'^itr/filing',views.itrdecide,name='decide'),
    url(r'^company/dashboard',views.companydashboard,name='companydashboard'),
    url(r'^company/docs',views.companydocs,name='companydocs'),
    url(r'^company/checkout',views.companycheckout,name='companycheckout'),
    url(r'^company/progress',views.companyprogress,name='companyprogress'),
    url(r'^company/begin',views.compdecide,name='continue'),
    url(r'^contact',views.contact,name='contact')
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)