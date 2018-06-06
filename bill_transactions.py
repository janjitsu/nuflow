from bills import Bills
from transactions import Transactions


class BillTransactions:
    @staticmethod
    def get_all():
        bills_details = Bills().get_all_with_details()
        transactions = Transactions().get_all()

        for bill in bills_details:
            bill['bill']['transactions'] = []
            for line_item in bill['bill']['line_items']:
                for transaction in transactions:
                    if 'href' in line_item.keys() and transaction['href'] == line_item['href']:
                        bill['bill']['transactions'].append(transaction)

        return bills_details

    @staticmethod
    def get_last(bills_qty = 1):
        bills_details = Bills().get_last_with_details(bills_qty)
        transactions = Transactions().get_all()

        for bill in bills_details:
            bill['bill']['transactions'] = []
            for line_item in bill['bill']['line_items']:
                for transaction in transactions:
                    if 'href' in line_item.keys() and transaction['href'] == line_item['href']:
                        bill['bill']['transactions'].append(transaction)

        return bills_details
