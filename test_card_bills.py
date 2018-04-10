from pprint import pprint
from bills import Bills
from transactions import Transactions


bills_details = Bills().get_all_with_details()
transactions = Transactions().get_all()


for bill in bills_details:
    bill['bill']['transactions'] = []
    bill['bill']['payments'] = []
    for line_item in bill['bill']['line_items']:
        for transaction in transactions:
            if 'href' in line_item.keys() and transaction['href'] == line_item['href']:
                bill['bill']['transactions'].append(transaction)
    pprint(bill['bill']['transactions'])

