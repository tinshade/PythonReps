'''
####################################################################################
By : Abhishek Iyengar
GitHub: https://github.com/tinshade

Dependencies: requests and json packages with Python 3.x^

Description: A tool to fetch publically available information
of a given IP address.

Usage: <IN TERMINAL> python -i google.com(Or any external IP)

Disclaimer: I am not responsible for any troubles you cause
with this tool. This is strictly for educational purposes only!

####################################################################################
'''

import requests #To get the data from IP-API
import argparse # Just to make this into a command-line tool.
import json #To convert the response into JSON


#Main method
if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("-i", "--ipaddress", help = "IP Address to track") #CMD argument structure
	args = parser.parse_args()
	ip = args.ipaddress
	url = "http://ip-api.com/json/"+ip
	response = requests.get(url)
	data = response.json()
	print(data) #Can be changed to get specific values. Check the structure of the response!