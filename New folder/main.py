__author__ = 'BackOffice-3'


import requests
import json
import pytest


class getapi(object):
    def __init__(self,base_url):
        self.request = requests.get(base_url, headers={'Authorization': 'Token token=56e4d2697115a9bcda5c3b28e6076f3c'})
        self.status = 0
        self.row = None


    def to_generate_different_urls(self):
        r = self.request
        self.status =r.status_code
        return self.status

    def to_check_id(self):
        r =self.request
        data = []
        data = json.loads(r.text)
        for row in data:
            print(row['id'])
        return self.row


