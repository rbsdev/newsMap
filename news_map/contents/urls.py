from django.conf.urls import patterns, url
from contents import views


urlpatterns = patterns('',
  url(r'^$', views.index_view, name='index'),
  url(r'^news/(?P<total>\d{1,2})/$', views.news_view, name='news'),
  url(r'^agendas/(?P<total>\d{1,2})/$', views.agendas_view, name='agendas'),
  url(r'^places/(?P<total>\d{1,2})/$', views.places_view, name='places'),
)