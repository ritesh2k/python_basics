def arr_chunk(arr,chunk_size):

	chunk_holder=[]				#creating an empty array to hold the chunks

	for i in range(0,len(arr),chunk_size):		
		chunk=[ele for ele in arr[i:i+chunk_size]]			#using list comprehension to divide the array into chunks

		chunk_holder.append(chunk)							#pushing the chunk into the chunk holder array

	print chunk_holder										

arr = list()
num = input("Enter how many elements you want in the array:")
print 'Enter numbers in array: '
for i in range(int(num)):
    n = input("num :")
    arr.append(int(n))

chunk_size=int(input('Enter the size the array needs to be divided into:\n'))    
arr_chunk(arr,chunk_size)
