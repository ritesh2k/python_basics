def fibonacci(num):
	if num==0: return 0
	elif num==1: return 1
	else:
				
		return fibonacci(num-1)+fibonacci(num-2)		#using recursion to generate the fibonacci series

num=int(input('How many fibonacci numbers do you want? \n'))
print('Fibonacci numbers are :\n')
for i in range(num):
	print(fibonacci(i) , end=' ')
print()	
