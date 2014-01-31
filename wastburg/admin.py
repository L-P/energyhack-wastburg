from django.contrib import admin
from models import *

class LotAdmin(admin.ModelAdmin):
  model = Lot
admin.site.register(Lot, LotAdmin)

class BuildingAdmin(admin.ModelAdmin):
  model = Building
admin.site.register(Building, BuildingAdmin)

class EnergyDayAdmin(admin.ModelAdmin):
  model = EnergyDay
  list_display = ('lot', 'day')
admin.site.register(EnergyDay, EnergyDayAdmin)
