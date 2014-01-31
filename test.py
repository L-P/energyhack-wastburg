import pprint
from api import EnergyApi

def test():
  ea = EnergyApi()
  params = {
    "prog":"CERGY01",
    "ctx":"GLOBAL",
    "ind":0,
    "gran":"LAST"
  }
  data = ea.request(params)
  pprint.pprint(data)

if __name__ == '__main__':
  test()
