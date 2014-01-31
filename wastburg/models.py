from django.db import models

class Building(models.Model):
  name = models.CharField(max_length=50, unique=True)
  prog = models.CharField(max_length=50)

  def __unicode__(self):
    return '%s/%s' % (self.prog, self.name)

class Lot(models.Model):
  building = models.ForeignKey(Building)
  name = models.CharField(max_length=50, unique=True)
