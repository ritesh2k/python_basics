def fizz_buzz(num):
	for i in range(1,num+1):
		if i%15==0:						#checking if the number is divisible by both 3 and 5
			print ('Fizzbuzz')
		elif i%5==0:
			print('buzz')
		elif i%3==0:
			print('fizz')
		else:
			print(i)
num= int(input('Enter the range of numbers\n'))
fizz_buzz(num)