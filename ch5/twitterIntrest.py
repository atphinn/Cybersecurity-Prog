import json
import re
import urllib
import urllib2
import optparse

from anonBrowser import *

def get_tweets(handle):
    query = urllib.parse.quote_plus('from:' + handle+ 'since:2009-01-01 include:retweets')
    tweets = []

    browser = anonBrowser()
    browser.anonmyize()

    response = browser.open('http://search.twitter.com/' + \
        'search.json?q=' + query)

    json_objects = json.load(response)

    for result in json_objects['results']:
        new_result = {}
        new_result['from_user'] = result['from_user_name']
        new_result['geo'] = result['geo']
        new_result['tweet'] = result['text']
        tweets.append(new_result)
    return tweets

def find_intrest(tweets):
    intrests = {}
    intrests['links'] = []
    intrests['users'] = []
    intrests['hashtags'] = []
    
    for tweet in tweets:
        text = tweet['tweet']
        links = re.compile('(http.*?)\Z|(http.*?)')\
            .findall(text)
        
        for link in links:
            if link[0]:
                link = link[0]
            elif link[1]:
                link = link[1]
            else:
                continue
            
            try:
                response = urllib2.urlopen(link)
                full_link = response.url
                interest['links'].append(full_link)
            
            except:
                pass
            
            intrests['users'] += re.compile('(@\w+)').findall(text)
            intrests['hashtags'] +=\
                re.compile('(#\w+)').findall(text)
            
            intrests['user'].sort()
            intrests['hashtags'].sort()
            
            return intrests

def main():
    parser = optparse.OptionParser('usage%prog' +\
        '-u <twitter handle>')
    
    parser.add_option('-u', dest='handle', type='string',
                      \
                          help= 'specify twitter handle')
    
    (options, args) = parser.parse_args()
    
    handle = options.handle
    
    if handle == None:
        print(parser.usage)
    exit(0)
    
    tweets = get_tweets(handle)
    intrest = find_intrest(tweets)
    
    print('\n[+] Links.')
    
    for link in set(intrest['links']):
        print('[+]' + str(link))
    
    print('\n[+] Users.')
    
    for user in set(intrest['users']):
        print('[+]' + str(user))
    print('\n[+] HashTags.')
    
    for hashtag in set(intrest['hashtags']):
        print('[+]' + str(hashtag))

if __name__ == '__main__':
    main()
    
            




 