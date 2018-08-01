# This class will fetch a Pynubank class with user credentials
import json
from pynubank import Nubank

class MyNubank:
    def __new__(self):
        credentials = json.load(open('credentials/nubank_credentials.json'))
        return Nubank(credentials['cpf'],credentials['password'])

if __name__ == '__main__':
    from pprint import pprint

    my_nubank = MyNubank();
    pprint(my_nubank)
