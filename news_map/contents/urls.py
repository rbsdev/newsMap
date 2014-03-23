from django.conf.urls import patterns, url
from contents import views


urlpatterns = patterns('',
  url(r'^$', views.index_view, name='index'),
  url(r'^news/(?P<total>\d{1,2})/$', views.news_view, name='news'),
  url(r'^agendas/(?P<total>\d{1,2})/$', views.agendas_view, name='agendas'),
  url(r'^places/(?P<total>\d{1,2})/$', views.places_view, name='places'),
  url(r'^contents/$', views.contents_view, name='contents'),
  url(r'^new-detail/(?P<id>\d{1,4})/$', views.new_detail_view, name='new_detail'),
  url(r'^agenda-detail/(?P<id>\d{1,4})/$', views.new_agenda_view, name='new_agenda'),
)