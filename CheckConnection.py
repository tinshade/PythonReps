"""
Check Internet Connection With Python
Author:Abhishek Iyengar
GitHub: tinshade
YouTube: AnnoyingErrors

This little script tells you whether you are connected to the internet or not by trying to connection to a host using the
"Socket" module and returns True if active and False otherwise.

"""

import socket

def check_conn():
	try:
		socket.create_connection(("www.google.com", 80)) #Specifying Host with Port
		return True #Connection active
	except Exception as e:
		#print(e) #Printing Error Message(DEBUGGING)
		pass
	return False #Not connected


print(check_conn())