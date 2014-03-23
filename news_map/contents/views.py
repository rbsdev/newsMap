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
                          values('id', 'title', 'lat', 'lon', 'description')

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
  news = news_view(request, 10, False)
  agendas = agendas_view(request, 10, False)
  places = places_view(request, 10, False)

  total = {
    'news': news,
    'agendas': agendas,
    'places': places
  }

  data = json.dumps(total)

  return HttpResponse(data, mimetype='application/json')


def new_detail_view(request, id):
  new = New.objects.get(id=id)
  new.__dict__.pop('_state', None)
  new.__dict__.pop('date', None)
  new.__dict__.pop('image', None)

  data = json.dumps(new.__dict__)

  return HttpResponse(data, mimetype='application/json')

def new_agenda_view(request, id):
  agenda = Agenda.objects.get(id=id)
  agenda.__dict__.pop('_state', None)
  agenda.__dict__.pop('start_date', None)
  agenda.__dict__.pop('finish_date', None)

  data = json.dumps(agenda.__dict__)

  return HttpResponse(data, mimetype='application/json')
