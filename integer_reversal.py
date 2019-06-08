def int_reversal(num):
	rev_num=0
	sign=1
	if num<0:
		sign=-1
		num=num*sign	
	while (num>0):
		rev_num=rev_num*10+(num%10) #taking the last digit of the numberm
		num=num//10					#removing the last digit from the number
	return rev_num*sign
num = int(input('Enter the number to be reversed:\n'))
print('The original number is: ',num)
print('The reversed number is:',int_reversal(num))		