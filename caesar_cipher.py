def encrypt(text, s):
    result = ""
    for i in range(len(text)): 
        char = text[i] 
        if (char.isupper()): 
            result += chr((ord(char) + s-65) % 26 + 65) 
        else: 
            result += chr((ord(char) + s - 97) % 26 + 97)
    return result 
def decrypt(returened_result):
    print("Deciphered : " + returened_result)
def main():
    print("Enter text")
    text = input()
    print ("Text  : " + text)
    print("Enter s")
    s = int(input()) 
    print ("Shift : " + str(s))
    text2 = encrypt(text, s)
    print("Ciphered : " + text2)
    decrypt(encrypt(text2, 26-s))
if __name__ == "__main__":
    main()