from django.core.management.base import BaseCommand
from matplotlib import pyplot
from sklearn.svm import SVR
from wastburg.models import EnergyDay
import math
import numpy as np

DJU = [
    407.0, 339.4, 273.1, 209.7, 104.0, 30.3,
    14.3, 6.4, 57.6, 154.1, 307.4, 386.1
]

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
        #pyplot.plot_date(time. data, '-', c="r", xdate=True, ydate=False, label="temp")
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
        for eday in EnergyDay.objects.filter(lot__name=lot_name):
            if is_float_empty(eday.temper) or is_float_empty(eday.elec):
                continue

            cost = (eday.elec * self.COST_KWH)
            if(cost == 0):
                continue

            data.append(np.array([
                #float(eday.temper),
                DJU[eday.day.month - 1]
            ]))
            target.append(float(cost))
            time.append(eday.day)

        return (np.array(time), np.array(data), np.array(target))
