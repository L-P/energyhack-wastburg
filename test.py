import requests

class EnergyApi:
  url = 'https://camel.steria.fr:4043/CamelWebService/energy'
  login = 'NRJHack'
  password = 'x52jSh6Ur3S'

  def __init__(self):
    print self.url
    self.req = requests.get(self.url, auth=(self.login, self.password))

  def load(self):
    print 'Load'

if __name__ == '__main__':
  ea = EnergyApi()

