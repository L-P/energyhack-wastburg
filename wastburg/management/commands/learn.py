from django.core.management.base import BaseCommand
from matplotlib import pyplot
from sklearn.svm import SVR
from wastburg.models import EnergyDay, DjuDay, Lot
import math
import numpy as np

def is_float_empty(var):
    return not isinstance(var, float) or math.isnan(var)

class Command(BaseCommand):
    # http://www.fournisseurs-electricite.com/comparatif-electricite/actu-electricite/1082-prix-dun-kwh-delectricite-en-france
    COST_KWH = 0.1372

    def handle(self, *args, **options):
        lot = "A201"
        time, data, target = self.get_lot_training_set(lot)
        self.plot(time, data, target, lot)


    def plot(self, time, data, target, title):
        clf = SVR(probability=True)
        clf.fit(data, target)

        svr = clf.predict(data)

        pyplot.hold(True)
        pyplot.plot_date(time, target, '-', c="g", xdate=True, ydate=False, label="conso")
        pyplot.plot_date(time, svr, '-', c="b", xdate=True, ydate=False, label="SVR")

        pyplot.xlabel("day")
        pyplot.ylabel("conso")
        pyplot.title(title)
        pyplot.legend()
        pyplot.show()


    def get_lot_training_set(self, lot_name):
        data = []
        target = []
        time = []
        lot = Lot.objects.get(name=lot_name)

        for eday in EnergyDay.objects.filter(lot=lot):
            if is_float_empty(eday.temper) or is_float_empty(eday.elec):
                continue

            dju = None
            try:
                dju = DjuDay.objects.get(day=eday.day).dju
            except:
                continue

            cost = (eday.elec + (lot.DJU_TO_KWH * dju)) * self.COST_KWH
            data.append(np.array([
                eday.temper,
                lot.surface,
                dju
            ]))
            target.append(float(cost))
            time.append(eday.day)

        return (np.array(time), np.array(data), np.array(target))
