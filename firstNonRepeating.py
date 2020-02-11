#Find the first non-repeating character from a string.
#'aaabcdecdde' -> b



s = str(input("Enter a string: "))
for each in s:
	if each in s[s.index(each)+1::]:
		pass
	else:
		print(each)

