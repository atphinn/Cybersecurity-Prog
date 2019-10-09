import urllib, json
from anonBrowser import *

def google(search_term):
    ab = anonBrowser()
    search_term = urllib.parse.quote_plus(search_term)

    response = ab.open('http://ajax.googleapis.com/' +\
    'ajax/services/search/web?v=1.0&q=' + search_term)
    
    objects = json.load(response)
   
    print(objects)

google('Boondocks Saints')

