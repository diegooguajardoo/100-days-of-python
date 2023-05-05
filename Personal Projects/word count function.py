def cap(alias):
	word = alias
	count = 0
	for letter in word:
		if letter =="a":
			count = count + 1
	print(count)

word = input("Type any word: ")
cap(word)