import sys
import json
import pygsheets
from cache_request import CacheRequest
from os import path
from dateutil import parser
from pprint import pprint
from pynubank import Nubank
from datetime import datetime


cache = CacheRequest('get_card_bills')

if cache.has_cache():
    bills = cache.read_cache()
else:
    credentials = json.load(open('nubank_credentials.json'))
    nu = Nubank(credentials['cpf'],credentials['password'])
    bills = nu.get_card_bills()
    cache.save_cache(bills);

for bill in bills['bills']:
   pprint(bill['state'])
