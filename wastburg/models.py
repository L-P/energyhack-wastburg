from django.db import models

class Building(models.Model):
  name = models.CharField(max_length=50, unique=True)
  prog = models.CharField(max_length=50)

  def __unicode__(self):
    return '%s/%s' % (self.prog, self.name)

class Lot(models.Model):
  building = models.ForeignKey(Building)
  name = models.CharField(max_length=50, unique=True)

  def __unicode__(self):
    return '%s/%s' % (self.building, self.name)

class EnergyDay(models.Model):
  lot = models.ForeignKey(Lot)
  day = models.DateField()

  # Energy data
  chauffage = models.FloatField(blank=True, null=True)
  ecs = models.FloatField(blank=True, null=True)
  refroid = models.FloatField(blank=True, null=True)
  ventil = models.FloatField(blank=True, null=True)
  ecl = models.FloatField(blank=True, null=True)
  res_pris = models.FloatField(blank=True, null=True)
  autre = models.FloatField(blank=True, null=True)
  temper = models.FloatField(blank=True, null=True)
  vecs = models.FloatField(blank=True, null=True)
  elec = models.FloatField(blank=True, null=True)
  vef = models.FloatField(blank=True, null=True)
  enr_prod = models.FloatField(blank=True, null=True)

  class Meta:
    unique_together = (('lot', 'day'),)
