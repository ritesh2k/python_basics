def pattern(n):
    for i in range(n):
        for j in range(i+1):
            print ('#', end =' ')
        print('')


n = int(input('Enter the number of rows\n'))
pattern(n)
