from django.db import models


class Tag(models.Model):
  name = models.CharField(max_length=50, unique=True)

  def __unicode__(self):
    return self.name


class Content(models.Model):
  tag = models.ForeignKey(Tag, null=True, blank=True)
  title = models.CharField(max_length=60)
  description = models.TextField(unique=True)
  video = models.CharField(max_length=300, null=True, blank=True)

  def __unicode__(self):
    return self.title


class New(Content):
  date = models.DateField(auto_now=True)
  lat = models.CharField(max_length=50, null=True, blank=True)
  lon = models.CharField(max_length=50, null=True, blank=True)

  class Meta:
    verbose_name = 'noticia'


class Agenda(Content):
  lat = models.CharField(max_length=50, null=True, blank=True)
  lon = models.CharField(max_length=50, null=True, blank=True)

  class Meta:
    verbose_name = 'agenda'


class Place(Content):
  class Meta:
    verbose_name = 'lugar'
