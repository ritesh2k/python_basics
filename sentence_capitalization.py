def capitalization(str):
	str=str.strip()
	cap=''
	for i in range(len(str)):
		if i==0 or str[i-1]==' ':cap=cap+str[i].upper()				#checking for the space and the first char of the sentence
		else: cap=cap+str[i]										#capitalizing the character after space
	
	#cap =[words[0].upper()+words[1:]]
	print ('The result is:\n{}'.format(cap))
str=input('Enter the sentence and each word will be capitalized:\n')
capitalization(str)