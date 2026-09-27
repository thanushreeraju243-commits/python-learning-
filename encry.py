import random
import string 
char = string.ascii_letters + string.digits + string.punctuation + string.whitespace
char = list(char)
key = char.copy()
random.shuffle(key)
plaintext = input("Enter the plaintext: ")
ciphertext = ""
for char in plaintext:
    index = char.index(char)
    ciphertext += key[index]
    
print(f"encrypted text: {ciphertext}")
print(f"message: {plaintext}")
