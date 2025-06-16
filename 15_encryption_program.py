import string
import random

chars = string.punctuation + string.digits + string.ascii_letters + " "

chars_list = list(chars)
random.shuffle(chars_list)

key = chars_list.copy()
random.shuffle(key)

print(f"chars : {chars_list}")
print(f"key   : {key}")

# Encryption
plain_text = input("Enter the text to encrypt: ")
chiper_text = ""

for letter in plain_text:
    if letter in chars_list:
        index = chars_list.index(letter)
        chiper_text += key[index]
    else:
        chiper_text += letter  # Just keep unknown characters as is

print("Encrypted:", chiper_text)

# Decryption
original_text = ""
for letter in chiper_text:
    if letter in key:
        index = key.index(letter)
        original_text += chars_list[index]
    else:
        original_text += letter  # Preserve unknown characters

print("Decrypted:", original_text)
