from django.db import models
from licence4.settings import KWH_TO_EUROS, DJU_TO_KWH
from datetime import timedelta
from django.db.models import Avg, Sum

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
  DJU_TO_KWH = 33.7

  def __unicode__(self):
    return '%s/%s' % (self.building, self.name)

  def calc_mean_cost(self):
    dju_total = sum([d.dju for d in DjuDay.objects.filter(day__year=2013)])
    return dju_total * DJU_TO_KWH * self.surface * KWH_TO_EUROS / 1000.0

  def check_season(self, day, days_before=60):
    '''
    Gives diff, average & current djus
    in comparison to previous years
    '''
    # Get current dju average values
    end = day
    start = day - timedelta(days=days_before)
    current_djus = DjuDay.objects.filter(day__gte=start, day__lte=end).order_by('day')
    return current_djus.aggregate(diff=Sum('diff'),average=Sum('average'),dju=Sum('dju'))

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
  average = models.FloatField(null=True)
  diff = models.FloatField(null=True)

  def calc_average_diff(self):
    avg = DjuDay.objects.filter(day__day=self.day.day, day__month=self.day.month).aggregate(Avg('dju'))
    self.average = avg['dju__avg']
    self.diff = self.dju - self.average
    return self.average, self.diff
