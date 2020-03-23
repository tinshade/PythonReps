"""
Author:Abhishek Iyengar
GitHub:tinshade
YouTube: Annoying Errors
DISCLAIMER : I DO NOT OWN ANY OF THE IMAGES YOU MIGHT DOWNLOAD USING THIS SCRIPT, NOR DO I TAKE ANY RESPONSIBILITY OF ANY
MISUSE OF THIS SCRIPT

This script adds to the startup and provides a new wallpaper from the internet every time the system boots up! All the images
are taken from Unsplash and all credits go the the respective authors!


"""


import ctypes #To set the wallpaper on Windows
from datetime import datetime #To give each download an unique name
from time import sleep #To pause for 5 seconds before setting the wallpaper
import requests #To stream the image from URL to local file
import os #To find the absolute path to the file and the image dynamically

import socket #To establish connection to a host to check for connectivity

import sys #For string formatting with slashes
import winreg as reg #To add registry keys

now = datetime.now() #Getting the current system's date and time
filename = str(now.strftime("%d%m%Y%H%M%S"))+".jpg" #Generating an unique filename based on the current date and time stamp
userPath = os.path.join(os.path.expandvars("%userprofile%"),"PresenceWallpaper") #Setting custom path to a folder in User's folder

#Function to start script on Windows boot
def addStartup():
	if os.path.exists(userPath) == True:
		pass #Already added to registry
	else:
		print("Creating folder")
		os.mkdir(userPath) #Creating the directory for future checking and wallpaper storage
		fp = os.path.dirname(os.path.realpath(__file__)) #Getting the real path to the current script
		file_name = sys.argv[0].split('\\')[-1] #Formatting the path to get the filename
		new_file_path = fp + '\\' + file_name #Generating new file path
		keyVal = r'Software\Microsoft\Windows\CurrentVersion\Run' #2nd half of registry key in Registry Editor (Can be changed to RunOnce)
		key2change = reg.OpenKey(reg.HKEY_CURRENT_USER, keyVal, 0, reg.KEY_ALL_ACCESS) #Adding keys with 1st and 2nd halves of the registry
		reg.SetValueEx(key2change, 'PresenceWallpaper', 0, reg.REG_SZ,new_file_path) #Setting path in the registry and finishing the addition

#Function to check internet connectivity
def check_conn():
	try:
		socket.create_connection(("www.google.com", 80)) #Specifying Host with Port
		return True #Connection active
	except Exception as e:
		#print(e) #Printing Error Message(DEBUGGING)
		pass
	return False #Not connected

#Function to download the image
def downloader():
	#Writing the file as bytes to JPG
	link = "https://source.unsplash.com/random"
	with open(userPath+"\\"+filename,'wb') as w:
		response = requests.get(link, stream=True) #Streaming is necessary
		if not response.ok:
			print(response) #If the response is not 200, the response will be printed
		#The chunk size of the image that is being downloaded is set to standard 1024Kbs
		for block in response.iter_content(1024):
			if not block:
				break #Breaks when the image is fully streamed

			w.write(block) #Writing the fully streamed image to the local storage

#Function to set the wallpaper on Windows
def setwall():
	sleep(5) #Waiting for 5s to allow pointer refreshing
	a_path = userPath+"\\"+filename #Creating the absolute path to the image
	ctypes.windll.user32.SystemParametersInfoW(20, 0, str(a_path), 0) #Setting the wallpaper
	print("Here's your wallpaper for the day!")

#Driver Code
def main():
	sleep(3) #Sleeping for at least 30s to allow for internet connection to be stable. Experiment with these values
	addStartup()
	if check_conn() != True:
		print("Please check your internet connection and try again..")
	else:
		try:
			downloader()
			setwall()
		except:
			#Printing a generic error message when I don't know what's wrong... :(
			print("Something went wrong. Make sure you are running as an 'Administrator' and have an active internet conneciton")


#Calling the driver code
main()