"""

Name: TinyLinker
By: Abhishek Iyengar
Description: Implementing pyshorteners module to create short links via TinyURL.
Other API services require registration and keys but can be made useful.


"""


import pyshorteners
def shortme():
	url = str(input("Enter the URL you need shortened: "))
	s = pyshorteners.Shortener()
	link=s.tinyurl.short(url)
	return link


if __name__ == "__main__":
	print(f"Here's your shortened link:{shortme()}")
