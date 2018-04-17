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
    date = bill['bill']['summary']['close_date']
    name = datetime.strptime(date,'%Y-%m-%d').strftime('%Y%B')
    pprint(bill['bill']['summary']['close_date'])
    if add_next:
        sheet = spreadsheet.add_worksheet(name)
    if (len(sheets) == 1 and not add_next):
        sheet = spreadsheet.sheet1
        sheet.title = name
        add_next = True

    transaction_rows = []
    for transaction in bill['bill']['transactions']:
        transaction_date = datetime.strptime(
            transaction['time'],
            "%Y-%m-%dT%H:%M:%SZ"
        ).strftime("%d/%m/%Y")
        transaction_rows.append([
            transaction_date,
            transaction['description'],
            transaction['title'],
            ",".join(transaction['details']['tags']),
            "%.2f" % (transaction['amount'] / 100)
        ])
    sheet.insert_rows(2,1,transaction_rows)


sys.exit(0)
# Extract and print all of the values
sheet.insert_rows(2,1,['25/02/2018','top sabor','restaurante','jan,karina'])
list_of_hashes = sheet.get_all_records()
print(list_of_hashes)
#print(nubank.worksheets())
#print(sheet.row_values(1))
#print(sheet.row_count())
# for bill create worksheet write summary on it
# print all transactions
