from anonBrowser import *

ab = anonBrowser(proxies = [], \
	user_agents = [('User-agent','superSecretBrowser')])

for attempt in range(1,5):
	ab.anonymize()
	print('[*] Frtching page')

response = ab.open('http://kittenwar.com')
for cookie in ab.cookie_jar:
	print(cookie)
