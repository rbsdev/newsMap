from django.db import models


class Tag(models.Model):
  name = models.CharField(max_length=50, unique=True)

  def __unicode__(self):
    return self.name


class Content(models.Model):
  tag = models.ForeignKey(Tag)
  title = models.CharField(max_length=50)
  description = models.TextField(unique=True)

  def __unicode__(self):
    return self.title


class New(Content):
  date = models.DateField(auto_now=True)
  lat = models.CharField(max_length=50, null=True)
  lon = models.CharField(max_length=50, null=True)


class Agenda(Content):
  lat = models.CharField(max_length=50, null=True)
  lon = models.CharField(max_length=50, null=True)


class Place(Content):
  pass
