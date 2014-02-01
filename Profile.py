from sklearn.externals import joblib

class Profile:
    cost = None # [doy, temp, lot.surface, dju] -> cost
    temp = None # [doy, dju] -> temp
    dju  = None # [doy] -> dju

    def __init__(self):
        self.cost = joblib.load("data/cost/dump")
        self.temp = joblib.load("data/temp/dump")
        self.dju  = joblib.load("data/dju/dump")

    def predict_cost(self, doys, surface):
        djus = self.dju.predict([[x] for x in doys])
        temps = self.temp.predict(zip(doys, djus))
        surfaces = [surface for x in doys]
        return self.cost.predict(zip(doys, temps, surfaces, djus))
