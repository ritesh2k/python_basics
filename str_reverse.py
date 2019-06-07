def str_rev(str):
	str_rev=''
	for char in str:
		str_rev= char+str_rev
	return str_rev

str=str(input('Enter the string to be reversed:\n'))
print(str_rev(str))