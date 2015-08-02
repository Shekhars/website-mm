from django.conf.urls import include, url
from mudramantri import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
admin.autodiscover()

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
    url(r'^contact',views.contact,name='contact'),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login'),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^weblog/', include('zinnia.urls', namespace='zinnia')),
    url(r'^comments/', include('django_comments.urls')),
    url(r'^ckeditor/', include('ckeditor.urls')),
    url(r'^privacy-and-terms/', views.privacy, name = 't&c'),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url(r'^extrainfo/',views.extrainfo, name='extrainfo'),
    url(r'^sociallogin/',views.sociallogin, name="social login"),
    url(r'^extra/',views.require_email, name='require_email'),
    url(r'^signup_complete/',views.sociallogin, name='signup complete')
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

blog_urls = [
    url(r'^', include('zinnia.urls.capabilities')),
    url(r'^search/', include('zinnia.urls.search')),
    url(r'^sitemap/', include('zinnia.urls.sitemap')),
    url(r'^trackback/', include('zinnia.urls.trackback')),
    url(r'^blog/tags/', include('zinnia.urls.tags')),
    url(r'^blog/feeds/', include('zinnia.urls.feeds')),
    url(r'^blog/random/', include('zinnia.urls.random')),
    url(r'^blog/authors/', include('zinnia.urls.authors')),
    url(r'^blog/categories/', include('zinnia.urls.categories')),
    url(r'^blog/comments/', include('zinnia.urls.comments')),
    url(r'^blog/', include('zinnia.urls.entries')),
    url(r'^blog/', include('zinnia.urls.archives')),
    url(r'^blog/', include('zinnia.urls.shortlink')),
    url(r'^blog/', include('zinnia.urls.quick_entry'))
]

url(r'^', include(blog_urls, namespace='zinnia'))
SOCIAL_AUTH_URL_NAMESPACE = 'social'
