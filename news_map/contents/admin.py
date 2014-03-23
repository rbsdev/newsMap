from django.contrib import admin
from contents.models import Tag, New, Agenda, Place


admin.site.register(Tag)
admin.site.register(New)
admin.site.register(Agenda)
admin.site.register(Place)