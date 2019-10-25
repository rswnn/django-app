from django.conf.urls import url
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^header/$', views.header, name='header'),
    url(r'^menu/$', views.menu, name='menu'),
    url(r'^home/$', views.home, name='home'),
    url(r'^profil/$', views.profil, name='profil'),
    url(r'^gallery/$', views.gallery, name='gallery'),
    url(r'^kontak/$', views.kontak, name='kontak'),
    url(r'^footer/$', views.footer, name='footer'),
    url(r'^$', views.index),
]
