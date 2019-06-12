def fibonacci(num):
	if num==0: return 0
	elif num==1: return 1
	else:
				
		return fibonacci(num-1)+fibonacci(num-2)

def fib_pyramid(step):
	print_num, spaces=0,0
	for i in range(step):					#outer loop to control the steps
		spaces=step-i-1						#controlling the spaces at the start of each steps
		print (' '*spaces, end='')
		for j in range(i+1):				#inner loop to call the fibonacci() function
			print(fibonacci(print_num), end=' ')
			print_num += 1
		print()

step=int(input('Enter the number of steps: '))	#driver code
fib_pyramid(step)		