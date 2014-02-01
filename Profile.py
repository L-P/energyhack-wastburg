from sklearn.externals import joblib

# [doy, temp, lot.surface, dju] -> cost
def get_cost_profile():
    return joblib.load("data/cost/dump")


# [doy] -> dju
def get_dju_profile():
    return joblib.load("data/dju/dump")


# [doy, dju] -> temp
def get_temp_profile():
    return joblib.load("data/temp/dump")
