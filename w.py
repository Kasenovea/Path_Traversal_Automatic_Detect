import urllib.parse
from  urllib.parse import urlparse, parse_qs
from  urllib.parse import urlencode



url="https://via.placeholder.com/490?id=ff&h1=33&h2=33&h3=33&h4=33"

query = urlparse(url).query
params = parse_qs(query)
print(query)
print('+++++++++',params)



#={'id': ['www'], 'f': ['3', '4', '6']}
for x in params:
	w=params[x]='../../etc/passwd'
	
	print('==',w)
	#print(x)
print(params)

query_string = urlencode(params)
print(query_string)





print(url + urllib.parse.urlencode(params))

#encoded_parms = urllib.parse.urlencode(n).encode('utf-8')
#tt=urllib.parse.urlencode(n)
#print('========',tt)
#
#print(encoded_parms)

