import sys
import json
import pygsheets
from cache_request import CacheRequest
from os import path
from dateutil import parser
from pprint import pprint
from pynubank import Nubank
from datetime import datetime

credentials = json.load(open('nubank_credentials.json'))
nu = Nubank(credentials['cpf'],credentials['password'])

cache = CacheRequest('get_card_bills')

if cache.has_cache():
    bills = cache.read_cache()
else:
    bills = nu.get_card_bills()
    cache.save_cache(bills);

for bill in bills['bills']:
    if bill['state'] == 'overdue':

        bill_cache = CacheRequest(bill['id'])

        if bill_cache.has_cache():
            bill_details = bill_cache.read_cache()
        else:
            bill_details = nu.get_card_bill_details(bill)
            bill_cache.save_cache(bill_details);
        pprint(bill_details)
