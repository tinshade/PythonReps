"""

Name: StatNet
By: AbhisheK Iyengar
Description: A small script to check your upload and download speed using Python.
A GUI based windows software version is available to download on my Electron repo!


"""

import speedtest #Speedtest module can also be using via CLI!
st = speedtest.Speedtest() #Making an instance of Speedtest

#Main function
def ischeck():
	#Try-Catch for exception handling
	try:	
		#Presenting options
		choice = int(input("""What do you want to check for?\n
		1. Download Speed
		2. Upload Speed
		> """))
		#Check for download speed
		if choice == 1:
			print(f"Your download speed is {st.download()/1000000}Mbps") #Feel free to trim the extra decimal points.
			return #Kill the process
		#Check for upload speed
		elif choice == 2:
			print(f"Your upload speed is {st.upload()/1000000}Mbps") #Feel free to trim the extra decimal points.
			return #Kill the process
		#If the user is dumb enough .... 
		else:
			print("Oops! That's not a valid option!\n")
			ischeck() #Recurse till killed or successful!
	except Exception as e:
		print("Looks like something went wrong... Are you connected to the Internet?")
	

#Checking if the file is called via CLI or from another file.
if __name__ =="__main__":
	ischeck()