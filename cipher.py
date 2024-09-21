# CustomKey not working if there are uppercase letters in the string
print('Enter your message:')
text = input()

print('Enter the key: ')
customKey = input()
#text = 'mrttaqrhknsw ih puggrur'
#customKey = 'python'

def vigenere(message, key, direction = 1):
    keyIndex = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    finalMessage = ''

    for char in message.lower():

        # Append any non-letter character to the message
        if not char.isalpha():
            finalMessage += char
        else:        
            # Find the right key character to encode/decode
            keyChar = key[keyIndex % len(key)]
            keyIndex += 1

            # Define the offset and the encrypted/decrypted letter
            offset = alphabet.index(keyChar)
            index = alphabet.find(char)
            shiftedIndex = (index + offset * direction) % len(alphabet)
            finalMessage += alphabet[shiftedIndex]
    
    return finalMessage

def encrypt(message, key):
    return vigenere(message, key)
    
def decrypt(message, key):
    return vigenere(message, key, -1)

print(f'\nEncrypted text: {text}')
print(f'Key: {customKey}')

enryption = encrypt(text, customKey)
print(f'\nEncrypted text: {enryption}')

decryption = decrypt(text, customKey)
print(f'\nDecrypted text: {decryption}\n')