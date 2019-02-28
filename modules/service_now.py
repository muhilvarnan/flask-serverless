"""
Service now API adapatr
"""
import requests


class Adapater(object):
    def __init__(self, domain_name):
        self.domain_name = domain_name

    def get_books(self):
        r = requests.get(self.domain_name + "/api/v0/isbn/9789000035526")
        return r.json()
