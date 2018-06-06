import re
import time
from my_nubank import MyNubank
from cache_request import CacheRequest

class Bills:
    @staticmethod
    def get_all():
        cache = CacheRequest('get_bills')

        if cache.has_cache():
            bills = cache.read_cache()
        else:
            nu = MyNubank()
            bills = nu.get_bills()
            cache.save_cache(bills)

        return bills

    @staticmethod
    def show(bill):
        bill_cache = CacheRequest(bill['id'])

        if bill_cache.has_cache():
            bill_details = bill_cache.read_cache()
        else:
            nu = MyNubank()
            bill_details = nu.get_bill_details(bill)
            bill_cache.save_cache(bill_details);

        return bill_details

    def process_bills_details(self, bills):
        bills_collection = []
        for bill in bills:
            if bill['state'] != 'future':
                if 'id' not in bill:
                    # find id by href
                    href = bill['_links']['self']['href']
                    matches = re.match(r'(^.*/accounts/([^/]+)/.*$)',href)
                    bill['id'] = matches.group(2)
                bills_collection.append(self.show(bill))
                time.sleep(1)

        return bills_collection

    def get_all_with_details(self):
        bills = self.get_all()
        return self.process_bills_details(bills)

    def get_last_with_details(self, bills_qty = 1):
        bills = self.get_all()
        return self.process_bills_details(bills[:bills_qty])
