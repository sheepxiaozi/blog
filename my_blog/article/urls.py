from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^index/$', views.index, name="index"),
    url(r'^detail/(?P<pk>\d+)/$', views.detail, name="detail"),
    url(r'^archives/$', views.archives, name='archives'),
    url(r'^about_me/$', views.about_me, name='about_me'),
    url(r'^tag(?P<tag>\w+)/$', views.search_tag, name='search_tag'),
    url(r'^search/$', views.blog_search, name='search'),
]

