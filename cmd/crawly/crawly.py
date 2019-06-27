
import requests
from enum import Enum

# bitcoin crawler
def checkBTC():
	response = requests.get('https://chain.so/api/v2/get_info/BTCTEST')
	if response.status_code == 200:
	    # everything went swimmingly                                                                                                                   
	    # parse the response as JSON
	    content = response.json()

	    print("Name:", content['data']['name'])
	    print("Total Blocks:", content['data']['blocks'])


	sender = '2N9GTegzFdJ1w15wyC7UHNwxrngxKFJiF8L'
	receiver = 'mkaWNj9JEh3gH4rrPnCkMRHzFYhRs2QDmT'
	minconfs = '1'
	req = 'https://chain.so/api/v2/address/BTCTEST/' + sender 
	response = requests.get(req)

	if response.status_code == 200:
		# everything went swimmingly                                                                                                                   
	    # parse the response as JSON
	    content = response.json()
	    if content['status'] != "fail":
		    print("Address:", content['data']['address'])
		    print("Pending Value:", content['data']['pending_value'])
		    print("Received Value:", content['data']['received_value'])
		    # txions = content['data']['txs']
		    # for t in txions: 
		    # 	receive
		    print("TXID:", content['data']['txs'][0]['txid'])
		    print("Received from Address:", content['data']['txs'][0]['outgoing']['outputs'][0]['address'])
	else:
		print("error")

# ethereum 
def checkRinkETH():
	print("Tomorrow!")

# driver 
checkBTC()