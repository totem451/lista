from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^crear$', views.crear, name='crear'),
    url(r'^archivar/(?P<id>[0-9])$', views.archivar, name='archivar'),
]