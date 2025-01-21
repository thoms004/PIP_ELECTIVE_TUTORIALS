print("MENU\n1.ENCRYPTION\n2.DECRYPTION\n3.EXIT")
choice=int(input("Enter choice: "))

if choice == 1: #ENCRYPTION
    text=str(input("Enter text to encrypt: "))
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

elif choice == 2: #DECRYPTION
    text=str(input("Enter text to decrypt: "))
    key = int(input("Enter key value: "))
    decrypted_text=""

    for char in text:
        if char.isalpha():
            shift = key%26
            if char.isupper():
                decrypted_text += chr((ord(char) - ord('A') - shift)%26 + ord('A')) 
            elif char.islower():
                decrypted_text += chr((ord(char) - ord('a') - shift)%26 + ord('a'))
        else:
            decrypted_text +=char
    print("Decrypted Text : " +decrypted_text)

elif choice ==3: #EXIT
    exit()

else:
    print("Invalid choice")