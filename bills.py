from my_nubank import MyNubank
from cache_request import CacheRequest

class Bills:
    @staticmethod
    def get_all():
        cache = CacheRequest('get_card_bills')

        if cache.has_cache():
            bills = cache.read_cache()
        else:
            nu = MyNubank()
            bills = nu.get_card_bills()
            cache.save_cache(bills)

        return bills

    @staticmethod
    def show(bill):
        bill_cache = CacheRequest(bill['id'])

        if bill_cache.has_cache():
            bill_details = bill_cache.read_cache()
        else:
            bill_details = nu.get_card_bill_details(bill)
            bill_cache.save_cache(bill_details);

        return bill_details

    def get_all_with_details(self):
        bills_collection = []
        bills = self.get_all()
        for bill in bills['bills']:
            if bill['state'] == 'overdue':
                bills_collection.append(self.show(bill))

        return bills_collection



