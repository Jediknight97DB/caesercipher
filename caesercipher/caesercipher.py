from decrypt import decrypt
from encrypt import encrypt    
from art import logo
runprogram = True

while runprogram == True:
    print(logo)
    enorde = input("Type encrypt or decrypt: ").lower()
    if enorde == "encrypt" or enorde ==  "encode":
        shifter = int(input("Type the shift number you wish to encrypt with: "))
        words = input("Type the sentence to encrypt: ")
        encrypted = encrypt(words,shifter)
        print(f"The encryption yeilded: {encrypted}")   
    elif enorde == "decrypt" or enorde == "decode":
        shifter = int(input("Type the shift number you wish to decrypt with: "))
        words = input("Type the sentence to decrypt: ")
        decrypted = decrypt(words,shifter)
        print(f"The decryption yeilded: {decrypted}") 
    else:
        print("You must type encrypt or decrypt or you can type encode or decode.")
    answer = input("Do you want the program to run again?(Y/N)").lower()
    if answer == "n":
        runprogram = False