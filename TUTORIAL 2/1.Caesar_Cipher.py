#ENCRYPTION
text=str(input("Enter a text: "))
key = int(input("Enter key value: "))
encrypted_text=""

for char in text:
    if char.isalpha():
        shift = key%26
        if char.islower():
            encrypted_text += chr((ord(char)-ord('a') + shift)%26 + ord('a'))
        elif char.isupper():
            encrypted_text += chr((ord(char) - ord('A') + shift)%26 + ord('A'))
    else:
        encrypted_text +=char

print("Encrypted Text : " +encrypted_text)
