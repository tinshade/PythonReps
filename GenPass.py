"""

Name: GenPass
By: Abhishek Iyengar
Description: This is a simple password generation tool with python.
You can have passwords generated from 10 to 24 characters.
This can be altered to higher/lower numbers too!
A GUI implementation in the form of website and a standalone desktop application
will be appended here soon!

"""


from string import punctuation, ascii_letters, digits #Assortment of ASCII characters for stronger random passwords
import random #To generate random combinations with SystemRandom()
import clipboard #To have some ease of use

def genpass(choice):
	combined = ascii_letters + digits + punctuation #Generating and storing the combined password
	#SYSTEMRANDOM IS NOT AVAILABLE ON ALL PLATFROMS
	secure_random = random.SystemRandom() #Genrating random choice based on system source
	if choice == 10:
		password10 = "".join(secure_random.choice(combined) for i in range(10)) #Upto 10 Characters
		print("HERE'S YOUR PASSWORD!")
		print(password10)#Printing 10 character password
		clipboard.copy(password10) #Saving the password in the clipboard!
		print("\nI have copied it to the clipboard for you! Just paste away!\n:)")
	elif choice == 14:
		password14 = "".join(secure_random.choice(combined) for i in range(14)) #Upto 14 Characters
		print("HERE'S YOUR PASSWORD!")
		print(password14)#Printing 14 character password
		clipboard.copy(password14) #Saving the password in the clipboard!
		print("\nI have copied it to the clipboard for you! Just paste away!\n:)")
	elif choice == 24:
		password24 = "".join(secure_random.choice(combined) for i in range(24)) #Upto 24 Characters
		print("HERE'S YOUR PASSWORD!")
		print(password24)#Printing 24 character password
		clipboard.copy(password24) #Saving the password in the clipboard!
		print("\nI have copied it to the clipboard for you! Just paste away!\n:)")
	else:
		print("Choose from 10, 14 or 24!")

if __name__ == "__main__":
	choice = int(input("Choose the length of your password:\n10\n14\n24\n>"))
	genpass(choice)