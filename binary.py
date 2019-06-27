def dec_to_binary(num):
	binary=''
	while(num>0):
		binary=str(num%2)+binary
		num=num//2	
	print (binary)
	
num=int(input('Enter the decimal number to convert to binary'))
dec_to_binary(num)		