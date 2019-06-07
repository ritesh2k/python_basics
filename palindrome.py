def check_palindrome(str):
	str_rev=''
	for char in str:
		str_rev= char+str_rev
	return str==str_rev


str=input('Enter the string to check for palindrome:\n')
print(check_palindrome(str))