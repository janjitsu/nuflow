# This class will fetch a Pynubank class with user credentials
import json
from pynubank import Nubank

class MyNubank:
    def __new__(self):
        credentials = json.load(open('credentials/nubank_credentials.json'))
        return Nubank(credentials['cpf'],credentials['password'])
