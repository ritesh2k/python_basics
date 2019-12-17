def print_pattern(num):
  for i in range(num):
    if (i==0 or i==num-1):
      print (" "*(num-i-1)+"*"*num)    
    else:
      print (" "*(num-i-1)+"*"+" "*(num-2)+"*")  


num = int(input('Enter the string to be reversed:\n'))

print_pattern(num)