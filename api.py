import requests
import json

class EnergyApi:
  url = 'https://camel.steria.fr:4043/CamelWebService/energy'
  login = 'NRJHack'
  password = 'x52jSh6Ur3S'

  def request(self, params={}):
    payload = {
      "jsonrpc":"2.0",
      "method":"energy",
      "params" : [params,],
      "id":"energyhack007",
    }
    self.req = requests.post(self.url, auth=(self.login, self.password), verify=False, data = json.dumps(payload))
    data = self.req.json()
    return data['result']
