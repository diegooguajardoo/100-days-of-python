alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

if shift > 26:
	shift = shift % 26

def caesar(text, shift, direction):
	cipher_text = ""
	for i in text:
		if i in alphabet:
			position = alphabet.index(i)

			if direction == "encode":
				newposition = position + shift
			elif direction == "decode":
				newposition = position - shift
			
			if newposition > (len(alphabet)-1):
				newposition = newposition - len(alphabet)
			cipher_text += (alphabet[newposition])
		else:
			cipher_text += i

	print(cipher_text)


caesar(text,shift, direction)