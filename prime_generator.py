def prime(n):               # function to check if a number is prime or not
  if n<=1:
    return False
  elif n==2:
     return True 
  else:
     for i in range(2,n//2+1):    # checking for divisibility till the half of that number
       if n%i==0:
         return False
     return True



def iteration(count):
  n=2
  while count>0:                #calling the prime function for the desired number of times
    if prime(n):
      print (n,end=' ')
      count-=1
    n+=1  
count=int(input('How many prime numbers do you want? '))
print('Your list of prime numbers is : ', end='')    
iteration(count)
print()