def fibonacci(num):
	if num==0: return 0
	elif num==1: return 1
	else:
				
		return fibonacci(num-1)+fibonacci(num-2)

def fib_pyramid(step):
	print_num=0
	for i in range(step):
		for j in range(i+1):
			print(fibonacci(print_num), end=' ')
			print_num += 1
		print()

step=int(input('Enter the number of steps: '))
fib_pyramid(step)		