def fib_for(num):
	a,b=1,1
	for i in range(num):
		print (a, end=',')
		a,b=b,a+b

num = int(input("How many numbers in fibonacci series do you want?\n"))
print('The series is: '	)
fib_for(num)
print()
