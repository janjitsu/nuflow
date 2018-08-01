from my_nubank import MyNubank
from cache_request import CacheRequest

class Transactions:
    @staticmethod
    def get_all():
        cache = CacheRequest('get_card_statements')

        if cache.has_cache():
            transactions = cache.read_cache()
        else:
            nu = MyNubank()
            transactions = nu.get_card_statements()
            cache.save_cache(transactions)

        return transactions


if __name__ == '__main__':
    from pprint import pprint

    transactions = Transactions.get_all()
    pprint(transactions)
