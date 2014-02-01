from django.core.management.base import BaseCommand
from sklearn.externals import joblib
from sklearn.svm import SVR
from wastburg.models import EnergyDay, DjuDay
import math
import numpy as np

def doy_from_date(date):
    return date.timetuple().tm_yday

def is_float_empty(var):
    return not isinstance(var, float) or math.isnan(var)

class Command(BaseCommand):
    # http://www.fournisseurs-electricite.com/comparatif-electricite/actu-electricite/1082-prix-dun-kwh-delectricite-en-france
    COST_KWH = 0.1372

    def handle(self, *args, **options):
        cost_clf, temp_clf = self.get_global_cost_temp_profile()
        joblib.dump(cost_clf, "data/cost/dump")
        joblib.dump(temp_clf, "data/temp/dump")

        dju_clf = self.get_global_dju_profile()
        joblib.dump(dju_clf, "data/dju/dump")


    def get_global_dju_profile(self):
        data = []
        target = []

        for dju in DjuDay.objects.all():
            data.append(np.array([doy_from_date(dju.day)]))
            target.append(dju.dju)

        clf = SVR(probability=True)
        clf.fit(data, target)
        return clf


    def get_global_cost_temp_profile(self):
        cost_data = []
        cost_target = []
        temp_data = []
        temp_target = []

        for eday in EnergyDay.objects.all():
            if is_float_empty(eday.temper) or is_float_empty(eday.elec):
                continue

            dju = None
            try:
                dju = DjuDay.objects.get(day=eday.day).dju
            except:
                continue

            cost = (eday.elec + (eday.lot.DJU_TO_KWH * dju)) * self.COST_KWH
            doy = doy_from_date(eday.day)
            cost_data.append(np.array([
                doy,
                eday.temper,
                eday.lot.surface,
                dju
            ]))
            cost_target.append(cost)

            temp_data.append(np.array([
                doy,
                dju
            ]))
            temp_target.append(eday.temper)

        cost_clf = SVR(probability=True)
        cost_clf.fit(cost_data, cost_target)
        temp_clf = SVR(probability=True)
        temp_clf.fit(temp_data, temp_target)
        return (cost_clf, temp_clf)
