from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from django.contrib import admin
from dapp.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home, name='home'),
    url(r'delete/(\d+)/$', delete, name='del'),
    url(r'edit/(\d+)/$', edit, name='edit'),
    url(r'profile1/(\d+)/$', profile1, name='profile1'),
    url(r'^search/$', search, name='search'),
    url(r'^friends/$', friends, name='friend'),
    url(r'^profile/$', profile, name='profile'),
    url(r'^password/$', password, name='pass'),
    url(r'^register/$', register, name='register'),
    url(r'^check/$', check, name='check'),
    url(r'^index/$', index,name='index'),
    url(r'^logout/$', logout, name='logout'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
