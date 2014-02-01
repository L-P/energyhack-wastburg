from django.core.management.base import BaseCommand, CommandError
from wastburg.models import *
import os
import csv

class Command(BaseCommand):

  def handle(self, *args, **options):
    if len(args) != 1:
      raise CommandError('Specify a path')

    path = args[0]
    if not os.path.exists(path):
      raise CommandError('Invalid path %s' % path)

    with open(path, 'r') as csvlots:
      lots = csv.reader(csvlots)
      for lot in lots:
        self.import_lot(lot)

  def import_lot(self, data):
    '''
    Import a lot from CSV data
    '''
    build, _ = Building.objects.get_or_create(name=data[0])
    lot, _ = Lot.objects.get_or_create(building=build, name=data[1])
    floor_index = data[3] != 'RDC' and int(data[3]) or 0
    floor, _ = BuildingFloor.objects.get_or_create(building=build, floor=floor_index)
    lot.rooms = int(data[2][1])
    lot.floor = floor
    lot.size = float(data[5])
    lot.price = float(data[10])
    lot.save()
