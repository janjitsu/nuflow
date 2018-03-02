import json
from pprint import pprint
from pynubank import Nubank

credentials = json.load(open('nubank_credentials.json'))

print(credentials)

nu = Nubank(credentials['cpf'],credentials['password'])

transactions = nu.get_account_statements()

for entry in transactions:
    row = [entry['time'], entry['title'], entry['description'], entry['amount']]
    if 'tags' in entry['details']:
        row.append(entry['details']['tags'])
    pprint(row)
