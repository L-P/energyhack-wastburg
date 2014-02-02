from sklearn.externals import joblib
from wastburg.models import DjuDay
from licence4.settings import KWH_TO_EUROS, DJU_TO_KWH
import numpy as np

class Profile:
    cost = None # [doy, temp, lot.surface, dju] -> cost
    temp = None # [doy, dju] -> temp
    dju  = None # [doy] -> dju

    def __init__(self):
        self.cost = joblib.load("data/cost/dump")
        self.temp = joblib.load("data/temp/dump")
        self.dju  = joblib.load("data/dju/dump")


    def get_goal(self, surface, dates):
        """Return the spending goal for the current year."""
        return sum([v for d,v in self.get_daily_goals(surface, dates)])


    def get_bullshit_heat_spendings(self, surface, mu, sigma):
        heat = self.get_daily_goals(surface)
        noise = np.random.normal(mu, sigma, len(heat))
        return map((lambda x,y: x+y), noise, heat)


    def get_daily_goals(self, surface, dates):
        """
        Return a list of amounts, one per day, of average spending.
        @return float[] in euro
        """
        iterator = DjuDay.objects.filter(day__in=dates).order_by('day')
        return [
            [x.day, x.average * DJU_TO_KWH * KWH_TO_EUROS * surface / 1000] for x in iterator
        ]


    def predict_costs(self, doys, surface):
        """
        Predict the spendings for 365 days.
        @return float[] in euro
        """
        djus = self.dju.predict([[x] for x in doys])
        temps = self.temp.predict(zip(doys, djus))
        surfaces = [surface for x in doys]
        return self.cost.predict(zip(doys, temps, surfaces, djus))
