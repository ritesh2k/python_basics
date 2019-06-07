def rev_pyramid(steps):
	k=0
	for i in range(steps):
		for j in range(k):
			print(' ', end='')
		k+=1
		for j in range(steps-i):
			print('#',end=' ')
		print()



def pyramid(n):
	k=n-1
	for i in range(n):

		for j in range(k):
			print (' ', end='')
		k= k-1
		for j in range (i+1):
			print ('#', end=' ')
		print()
	

steps=int(input('Enter the number of steps\n'))
rev_pyramid(steps)
pyramid(steps)	