from django.core.management.base import BaseCommand, CommandError
from wastburg.models import *
import os
import math
import csv
from datetime import *
import random

class Command(BaseCommand):
  days = []

  def handle(self, *args, **options):
    start = date(2013, 1, 1)
    self.days = [start + timedelta(days=i) for i in range(0,365)]
    lots = Lot.objects.all()
    for lot in lots:
      self.fix_lot(lot)

  def fix_lot(self, lot):
    print lot
    for day in self.days:
      ed, _ = EnergyDay.objects.get_or_create(lot=lot, day=day)
      save = False
      d = day.timetuple().tm_yday
      if ed.temper is None:
        save = True
        ed.temper = math.sin(d*3.14/365) * 2.0 + 20
        print " > %s Fix temper %f" % (day, ed.temper)

      if ed.elec is None:
        save = True
        ed.elec = random.randint(1,1500)/1000.0
        print " > %s Fix elec %f" % (day,ed.elec)

      if save:
        ed.save()
