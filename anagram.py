def anagram(str):
	str=str.lower().replace(' ', '')		#converting to lowercase and removing spaces
	word_map={}
	for char in str:						#creating dictionary of the char
		if char in word_map:
			word_map[char]+=1
		else:
			word_map[char]=1	
	return word_map


def compare_word_map(first_word,second_word):
	return (anagram(first_word)==anagram(second_word))		#Returning the result of dictionary comparition

print('Welcome to Anagram Checker:\n')
first_word=input('Enter the first word: ')
second_word=input('Enter the second word: ')
print('Are the words anagram? ',compare_word_map(first_word,second_word))