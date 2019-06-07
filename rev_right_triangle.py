def rev_right_trian(steps):
	for i in range(steps): 					#Loop for controlling steps
		for j in range (steps-i):			#inner loop for controlling number of '#'
			print ('#', end=' ')
		print()								#moving to newling after an iteration of i

steps= int(input('Enter the number of steps\n'))
rev_right_trian(steps)