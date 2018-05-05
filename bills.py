import re
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

    def get_all_with_details(self):
        bills_collection = []
        bills = self.get_all()
        from pprint import pprint
        from os import sys
        for bill in bills:
            if bill['state'] != 'future':
                if 'id' not in bill:
                    # find id by href
                    href = bill['_links']['self']['href']
                    matches = re.match(r'(^.*/accounts/([^/]+)/.*$)',href)
                    bill['id'] = matches.group(2)
                bills_collection.append(self.show(bill))

        return bills_collection

