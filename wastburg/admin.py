from django.contrib import admin
from models import *

class LotAdmin(admin.ModelAdmin):
  model = Lot
admin.site.register(Lot, LotAdmin)

class BuildingAdmin(admin.ModelAdmin):
  model = Building
admin.site.register(Building, BuildingAdmin)
