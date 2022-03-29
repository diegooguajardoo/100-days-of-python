alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(text, shift):
	cipher_text = ""
	for i in text:
		position = alphabet.index(i)
		newposition = position + shift
		if newposition > (len(alphabet)-1):
			newposition = newposition - len(alphabet)
		cipher_text += (alphabet[newposition])
	print(cipher_text)

encrypt(text, shift)
