from django.core.management.base import BaseCommand, CommandError
from wastburg.models import *
import os
import csv
from datetime import datetime

class Command(BaseCommand):

  def handle(self, *args, **options):
    if len(args) != 1:
      raise CommandError('Specify a path')

    path = args[0]
    if not os.path.exists(path):
      raise CommandError('Invalid path %s' % path)

    with open(path, 'r') as csvdju:
      djus = csv.reader(csvdju)
      for dju in djus:
        self.import_dju(dju)

  def import_dju(self, data):
    '''
    Import a DJU from CSV data
    '''
    print data
    day = datetime.strptime(data[0],'%Y-%m-%d').date()
    val = float(data[1])
    dju, created = DjuDay.objects.get_or_create(day=day, defaults={'dju':val})
    if not created:
      dju.dju = val
      dju.save()
