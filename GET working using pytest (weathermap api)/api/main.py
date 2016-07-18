import requests
import json

class getapi(object):

    def __init__(self,baseurl,urlparam):
        self.request1 = requests.get(baseurl+urlparam+'&appid=6ceac7294286140698fbb9c2809b3a60')
        self.baseurl = baseurl
        self.urlparam = urlparam
        self.data = None
        self.status = 0
        self.url = None
        self.country = None
        self.state = None

    def to_generate_different_urls(self): 
        r = self.request1
        self.status =r.status_code
        return self.status

    def to_store_reponse(self):
        r = self.request1
        self.data = r.text
        print("Done!...Checking for", self.urlparam)
        return self.data

    def validate_params(self):
        r = self.request1
        self.url = r.url
        print("The URL's generated for the parameters :", self.urlparam)
        return self.url

    def validate_country(self):
        r = self.request1
        r = r.json()
        json_string = json.dumps(r)
        data = json.loads(json_string)
        self.country = data['sys']['country']
        print("The country located in the API :")
        return self.country

    def validate_location(self):
        r = self.request1
        r = r.json()
        json_string = json.dumps(r)
        data = json.loads(json_string)
        self.state = data['name']
        print("The state located in the API :")
        return self.state

    def validate_lonlat(self):
        r1 = self.request1
        r2 = r1.json()
        json_string = json.dumps(r2)
        data = json.loads(json_string)
        self.lon = data['coord']['lon']
        self.lat = data['coord']['lat']
        print("The longitude and latitude is")
        return self.lon,self.lat








