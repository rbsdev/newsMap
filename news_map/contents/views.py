import json
from django.shortcuts import render_to_response

def index(request):
  return render_to_response('contents/index.html')

def news(request):
  pass