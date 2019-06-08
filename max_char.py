def max_char(str):
	dict={}
	max=0
	max_char=''
	for char in str:
		if char in dict:
			dict[char]+=1		#checking if the key is already in dictionary
		else:
			dict[char] =1		# incrementing the value of the key by 1
	
	for key in dict:
		if max<dict[key]:
			max=dict[key]
			max_char=key
	return max_char,max 		#returning a tuple results		
str=str(input('Enter the string to find the most frequent char\n')).replace(' ','') # removing the spaces
print('The entered after removing spaces is :',str)
print('The most frequent character is \'{}\' which appears {} times.'.format(max_char(str)[0],max_char(str)[1])) # using \ to insert ''
