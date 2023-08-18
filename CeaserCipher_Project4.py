variable=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
def encryption(plain_text,shift_key):
     cipher_text=""
     for c in text:
         position=variable.index(c)
         new_position=(position+key)%26
         cipher_text+=variable[new_position]
     print(f'Cipher text is {cipher_text}')     

def decryption(plain_text,shift_key):
    decipher_text=""
    for c in text:
        position=variable.index(c)
        new_position=(position-key)%26
        decipher_text+=variable[new_position]
    print(f'Decipher text {decipher_text}')  

chioce=input("Enter type of operation do you want tp perform encrypt or decrypt : ")
text=input("Enter text : ")
key=int(input("Enter key for encryption : "))
if chioce=="encrypt":
    encryption(plain_text=text,shift_key=key)
elif chioce=="decrypt":
    decryption(plain_text=text,shift_key=key)
else:
    print("enter proper spelling")        
