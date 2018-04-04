import os
import pickle
from pprint import pprint

class CacheRequest:
    def __init__(self, cache_name):
        self.cache_dir = 'cache'
        self.filename = cache_name

    def get_file_path(self, filename=None):
        filepath = filename or self.filename
        return '%s/%s.dat' % (self.cache_dir, filepath)

    def save_cache(self, data):
        with open(self.get_file_path(), 'wb') as handle:
            pickle.dump(data, handle, protocol=pickle.HIGHEST_PROTOCOL)

    def read_cache(self):
        with open(self.get_file_path(), 'rb') as handle:
            return pickle.load(handle)

    def has_cache(self, cache_name=None):
        cache_name = cache_name or self.filename
        filepath = self.get_file_path(cache_name)
        return os.path.isfile(filepath)
