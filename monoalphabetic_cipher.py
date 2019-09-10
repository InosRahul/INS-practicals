keys={'a': 'X','b': 'D','c': 'G','d': 'S','e': 'Z','f': 'A','g': 'N','h': 'Y','i': 'O','j': 'B','k': 'T','l': 'M','m': 'J','n': 'C','o': 'E','p': 'V','q': 'F','r': 'H','s': 'K','t': 'W','u': 'P','v': 'L','w': 'Q','x': 'U','y': 'R','z': 'I',' ': ' ',}
reverse_keys={}
for key,value in keys.items():
    reverse_keys[value]=key
def encrypt(text):
    text=str(text)
    encrypting=[]
    for l in text:
        encrypting.append(keys.get(l,l))
    encrypted_text = (''.join(encrypting))
    return encrypted_text
def decipher(encrypted_text):
    text=str(encrypted_text)
    #print(text)
    decrypted=[]
    for l in text:
        decrypted.append(reverse_keys.get(l,l))
    deciphered_text = (''.join(decrypted))
    return deciphered_text
def main():
    print("Enter text")
    text = input()
    print ("Text  : " + text)
    cipher = encrypt(text)
    print("Ciphered : " + cipher)
    decipher_text = decipher(cipher)
    print("Deciphered : " +decipher_text)
if __name__ == "__main__":
    main()