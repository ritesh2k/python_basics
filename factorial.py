def fact(num):
	if num<0:
		print ('No factorial of negative num.')
		return
	elif num==0:
		return 1
	else:
		fact=1
		while num>0:
			fact=fact*num
			num-=1
		return fact, 'factorial'

num= int(input('Enter a number to find out its factorial :'))				
print(fact(num))