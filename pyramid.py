def pyramid(steps):
	k=steps-1										#determining the number of spaces
	for i in range(steps):							#contolling the outer loop

		for j in range(k):
			print (' ', end='')
		k= k-1
		for j in range (i+1):
			print ('#', end=' ')
		print()                                     #print a new line after outer loop iteration

steps= int(input('Enter the number of steps\n'))
pyramid(steps)	
