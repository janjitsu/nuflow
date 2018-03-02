import json
import pygsheets
from pprint import pprint
from pynubank import Nubank

client = pygsheets.authorize(service_file='client_secret.json')
credentials = json.load(open('nubank_credentials.json'))
nu = Nubank(credentials['cpf'],credentials['password'])
transactions = nu.get_account_statements()

# Find a workbook by name and open the first sheet
# Make sure you use the right name here.
nubank = client.open("Nubank")
sheet = nubank.sheet1

for entry in transactions:
    row = [entry['time'], entry['title'], entry['description'], entry['amount']]
    if 'tags' in entry['details']:
        row.append(",".join(entry['details']['tags']))
    sheet.insert_rows(2,1,row)
