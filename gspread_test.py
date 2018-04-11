import pygsheets
from os import sys
from pprint import pprint
from bill_transactions import BillTransactions
from datetime import datetime

client = pygsheets.authorize(service_file='credentials/client_secret.json')

# Find a workbook by name and open the first sheet
# Make sure you use the right name here.

bills = BillTransactions.get_all()

#clear spreadsheet
spreadsheet = client.open("Nubank")
sheets = spreadsheet.worksheets()
for sheet in sheets:
    if (len(sheets) > 1):
        spreadsheet.del_worksheet(sheet)

add_next = False
for bill in bills:
    date = bill['bill']['summary']['open_date']
    name = datetime.strptime(date,'%Y-%m-%d').strftime('%Y%B')
    pprint(bill['bill']['summary']['open_date'])
    if (len(sheets) == 1):
        sheet = spreadsheet.sheet1
        sheet.title = name
        sheet.sync()
        add_next = True
    if add_next:
        sheet = spreadsheet.add_worksheet(name)


#sys.exit(0)
# Extract and print all of the values
sheet.insert_rows(2,1,['25/02/2018','top sabor','restaurante','jan,karina'])
list_of_hashes = sheet.get_all_records()
print(list_of_hashes)
#print(nubank.worksheets())
#print(sheet.row_values(1))
#print(sheet.row_count())
# for bill create worksheet write summary on it
# print all transactions
