import json
import urllib
import optparse
from anonBrowser import *

class Google_Result:
    def __init__(self, title, thext, url):
        self.title = title
        self.text = text
        self.url = url
        
    def __repr__(self):
        return self.title

    def google(search_term):
        ab = anonBrowser()
        search_term = urllib.parse.quote_plus(search_term)

        response = ab.open('http://ajax.googleapis.com/' +\
        'ajax/services/search/web?v=1.0&q=' + search_term)
        
        objects = json.load(response)
        results = []
        
        for result in objects['responseData']['results']:
            url = result['url']
            title = result['titleNoFomatting']
            new_gr = Google_Result(title, text, url)
            results.append(new_gr)
        
        return results
    
    def main():
        parser = optparse.OptionParser('usage%prog' +\
            '-k <Keywords>')
        
        parser.add_option('-k', dest='keyword', type='string',\
            help="Please input keyword")
        
        (options, args) = parser.parse_args()
        
        keyword = options.keyword
        
        if options.keyword == None:
            print(parser.usage)
            exit(0)
        
        else:
            results = google(keyword)
            print(results)

    if __name__ == '__main__':
        main()
    
    
    
        