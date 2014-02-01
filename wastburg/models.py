from django.db import models

class Building(models.Model):
  name = models.CharField(max_length=50, unique=True)
  prog = models.CharField(max_length=50)

  def __unicode__(self):
    return '%s/%s' % (self.prog, self.name)

class BuildingFloor(models.Model):
  building = models.ForeignKey(Building)
  floor = models.IntegerField()

  class Meta:
    unique_together = (('building', 'floor'),)

class Lot(models.Model):
  building = models.ForeignKey(Building, related_name='lots')
  name = models.CharField(max_length=50, unique=True)
  floor = models.ForeignKey(BuildingFloor)
  rooms = models.IntegerField()
  surface = models.FloatField()
  price = models.FloatField()

  def __unicode__(self):
    return '%s/%s' % (self.building, self.name)

  def calc_my_dju(self, dju_base):
    return 33.7 * dju_base * self.surface

class EnergyDay(models.Model):
  lot = models.ForeignKey(Lot, related_name='days')
  day = models.DateField()

  # Energy data
  elec = models.FloatField(blank=True, null=True)
  temper = models.FloatField(blank=True, null=True)
  vecs = models.FloatField(blank=True, null=True)
  vef = models.FloatField(blank=True, null=True)

  class Meta:
    unique_together = (('lot', 'day'),)

class DjuDay(models.Model):
  day = models.DateField(unique=True)
  dju = models.FloatField()
