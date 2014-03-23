import json
from django.http import HttpResponse
from django.shortcuts import render_to_response
from contents.models import New, Agenda, Place


def index_view(request):
  return render_to_response('contents/index.html')


def convert_to_json(obj):
  has_data = len(obj) > 0

  if not has_data:
    return HttpResponse(status=404)

  data = json.dumps(list(obj))

  return HttpResponse(data, mimetype='application/json')


def news_view(request, total=1, with_json=True):
  start = 0
  news = New.objects.all()[start:total].\
                          values('id', 'title', 'lat', 'lon')
  if with_json:
    return convert_to_json(news)

  return news


def agendas_view(request, total=1, with_json=True):
  start = 0
  agendas = Agenda.objects.all()[start:total].\
                          values('id', 'title', 'lat', 'lon', 'description',\
                                 'start_date', 'finish_date')

  if with_json:
    return convert_to_json(agendas)

  return agendas


def places_view(request, total=1, with_json=True):
  start = 0
  places = Place.objects.all()[start:total].\
                          values('id', 'title', 'lat', 'lon')

  if with_json:
    return convert_to_json(places)

  return places


def contents_view(request):
  news = news_view(request, 10, False)[0]
  agendas = agendas_view(request, 10, False)[0]
  places = places_view(request, 10, False)[0]

  total = {
    'news': news,
    'agendas': agendas,
    'places': places
  }

  data = json.dumps(total)

  return HttpResponse(data, mimetype='application/json')