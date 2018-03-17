import json
import pickle
import pygsheets
from os import path
from dateutil import parser
from pprint import pprint
from pynubank import Nubank
from datetime import datetime


SAVE_FILE = "nubank.dat"

if path.exists(SAVE_FILE):
    feed = pickle.load(open(SAVE_FILE,"rb"))
else:
    credentials = json.load(open('nubank_credentials.json'))
    nu = Nubank(credentials['cpf'],credentials['password'])
    feed = nu.get_account_feed()
    pickle.dump(transactions, open(SAVE_FILE,"wb"))

# Find a workbook by name and open the first sheet
# Make sure you use the right name here.
client = pygsheets.authorize(service_file='client_secret.json')
nubank = client.open("Nubank")

rows = []
pprint(list(set(entry['category'] for entry in feed['events'])))

bills = list(filter(lambda x: x['category'] in ('transactions') , feed['events']))

sheets  = []
rows = []
pprint(len(bills))
for entry in bills:
    date = parser.parse(entry['time'])
    row = [date.strftime('%d/%m/%Y'), entry['title'], entry['description'], float(entry['amount']/100),'']
    if entry['category'] == 'transaction' and 'tags' in entry['details']:
        row.pop()
        row.append(",".join(entry['details']['tags']))
    rows.append(row)
    #elif entry['category'] == 'bill_flow_closed':
    #    row = [entry['time'], entry['title'], entry['description'], entry['amount'],'']
    #    sheets.append(rows)
    #    rows = []
sheet = nubank.sheet1
sheet.insert_rows(0,1,['time','title','description','amount','tags'])
result = sheet.insert_rows(1,len(rows),rows)
pprint(len(sheets))
"""
i = 1
for sheet in sheets:
    new_sheet = nubank.add_worksheet('oi%s'%i)
    new_sheet.insert_rows(0,1,['time','title','description','amount','tags'])
    new_sheet.insert_rows(1,len(sheet),sheet)
    i = i + 1
    """
#row = [entry['time'], entry['title'], entry['description'], entry['amount']]
#if 'tags' in entry['details']:
#    row.append(",".join(entry['details']['tags']))
#else:
#    row.append("")
#rows.append(row)

#result = sheet.insert_rows(1,len(rows),rows)


#print(result)
