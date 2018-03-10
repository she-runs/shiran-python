
def is_palindrome(string):
	"""
	The fonctiun gets a string and returns True if the string is a palindrome 
	"""
	return string[:]==string[::-1]
	
def check_palindrome():
	"""
	Runs through all 6-digit numbers and checks the mentioned conditions.
	The function prints out the numbers that satisfy this condition. 
	Note: It should print out the first number (with a palindrome in its last 4 digits), 
	not all 4 "versions" of it.
	"""
	results =[]
	for i in range(100000, 1000000):
		if is_palindrome(str(i)[2:]):
			if is_palindrome(str(i+1)[1:]):
				if is_palindrome(str(i+2)[1:5]):
					if is_palindrome(str(i+3)[:]):
						results.append(i)
	print results
					
check_palindrome()