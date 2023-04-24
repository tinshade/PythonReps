import requests
import re

url = input("Enter the url to fetch links: ") # For e.g., https://www.youtube.com/watch?v=xO0id3Dvalw

req = requests.get(url).text

link_regex = re.compile('((https?):((//)|(\\\\))+([\w\d:#@%/;$()~_?\+-=\\\.&](#!)?)*)')
links = re.findall(link_regex, req)


for lnk in links:
	print(lnk[0])
