import json
from django.http import HttpResponse
from django.shortcuts import render_to_response
from contents.models import New

def index_view(request):
  return render_to_response('contents/index.html')

def news_view(request, total=1):
  start = 0
  news = New.objects.all()[start:total].\
                          values('id', 'title', 'lat', 'lon')

  if not news:
    return HttpResponse(status=404)

  data = json.dumps(list(news))

  return HttpResponse(data, mimetype='application/json')
