from django.db import models

class Tag(models.Model):
  name = models.CharField(max_length=50, unique=True)


class Content(models.Model):
  tag = models.ForeignKey(Tag)
  title = models.CharField(max_length=50)
  description = models.CharField(max_length=100, unique=True)


class New(Content):
  date = models.DateField()
  lat = models.IntegerField()
  lon = models.IntegerField()