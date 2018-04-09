from pprint import pprint
from bills import Bills
from transactions import Transactions


bills_details = Bills().get_all_with_details()
transactions = Transactions().get_all()
for bill in bills_details:
    for line_item in bill['bill']['line_items']:
        pprint(line_item['id'])
        t = next((transaction for transaction in transactions if transaction['id'] == line_item['id']))
        pprint(t)
        break
    break
