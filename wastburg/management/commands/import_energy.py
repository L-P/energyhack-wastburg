from django.core.management.base import BaseCommand, CommandError
from django.db.models import Max
from wastburg.models import *
from api import EnergyApi
from datetime import date, timedelta
import time

class Command(BaseCommand):

  api = None

  def handle(self, *args, **options):
    self.api = EnergyApi()

    # Get min start day
    start = date(year=2013, month=1, day=1)
    agg = EnergyDay.objects.all().aggregate(Max('day'))
    if 'day__max' in agg and agg['day__max']:
      start = agg['day__max']

    # Always end today !
    end = date.today()
    print 'Date interval %s > %s' % (start, end)

    buildings = Building.objects.all()

    day = start
    while day <= end:
      for build in buildings:
        self.import_day(build, day)
      day += timedelta(days=1)

  def import_day(self, building, day):
    '''
    Import a day of data for a building
    '''
    print "Building %s from %s" % (building, day)

    next_day = day + timedelta(days=1)
    payload = {
      "prog" : building.prog,
      "build" : building.name,
      "ctx":"GLOBAL",
      "ind":0,
      "gran":"DAY",
      "begin": int(time.mktime(day.timetuple())) * 1000,
      "end" : int(time.mktime(next_day.timetuple())) * 1000,
    }
    data = self.api.request(payload)

    for result in data:
      self.import_lot(building, day, result)
    print ' >> %d lots imported' % len(data)

  def import_lot(self, building, day, data):
    '''
    Import EnergyHack data for a building in a day
    '''
    # Get (or build) Lot
    lot, _ = Lot.objects.get_or_create(building=building, name=data['lot'])

    # Get (or build) energy day
    ed,_ = EnergyDay.objects.get_or_create(lot=lot, day=day)

    # Browse data fields
    for field in data['chs']:
      name = field['type'].lower()
      value = 0.0
      # Do an average of value, but we should always
      # only have one value here
      for v in field['vals']:
        value += v['val']
      value /= len(field['vals'])

      setattr(ed, name, value)

    # Save !
    ed.save()
