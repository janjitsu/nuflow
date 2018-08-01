from bills import Bills
from datetime import datetime
from transactions import Transactions
from pprint import pprint
from os import sys

class BillTransactions:
    @staticmethod
    def __process_bill_transactions(bills_details, transactions):
        for bill in bills_details:
            bill['bill']['transactions'] = []
            for line_item in bill['bill']['line_items']:
                for transaction in transactions:
                    if 'href' in line_item.keys() and transaction['href'] == line_item['href']:
                        # fix transactions with multiple charges
                        if 'charges' in line_item and line_item['charges'] > 1:
                            #pprint(line_item)
                            transaction['amount'] = line_item['amount']
                            transaction['time'] = line_item['post_date'] + "T00:00:00Z"
                            transaction['description'] = "%s (%s/%s)" % (line_item['title'], line_item['index']+1, line_item['charges'])

                        bill['bill']['transactions'].append(transaction)
        #sys.exit(0)
        return bills_details


    @staticmethod
    def get_all():
        bills_details = Bills().get_all_with_details()
        transactions = Transactions().get_all()

        return BillTransactions.__process_bill_transactions(bills_details, transactions)


    @staticmethod
    def get_last(bills_qty = 1):
        bills_details = Bills().get_last_with_details(bills_qty)
        transactions = Transactions().get_all()

        return BillTransactions.__process_bill_transactions(bills_details, transactions)

if __name__ == '__main__':

    pprint(BillTransactions.get_last(3))
