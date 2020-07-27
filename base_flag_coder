"""Built to decrypt/encrypt Base64 as many times as you want/need.
    I mainly built this for the CTF machines that
    I have ran into that require information to be decoded 10+ times.
    Also wanted to level up my python programming."""

import base64

def main():
    '''Choose encryption/decryption.'''
    mode = input("Please choose mode, [1]Encryption | [2]Decryption ('Q' to quit): ")
    try:
        if int(mode) == 1:
            #Run Encryption
            encrypt()
        elif int(mode) == 2:
            #Run Decryption
            decrypt()
    except ValueError:
        print("Thanks for using this program.")
        return None

def encrypt():
    '''Encrypts in base64'''
    message = input("Input the message you would like to encrypt: ")
    data = message.encode('utf-8')
    times_to_encrypt = input("Please enter number of times to encrypt[USE NUMBERS ONLY]: ")
    try:
        for i in range(0, int(times_to_encrypt)):
            data = base64.b64encode(data)
    except ValueError:
        print("Do not spell the number. Numeric input only. Example: 1, 10, 100, etc.")
    print(data)

def decrypt():
    '''Decrypt base64'''
    secret = input("Please insert encoded Base64 encoded message: ")
    data = secret
    times_to_decrypt = input("Enter number of times to decrypt[Use NUMBERS ONLY]: ")
    try:
        for i in range(0, int(times_to_decrypt)):
            data = base64.b64decode(data)
    except ValueError:
        print("Do not spell the number. Numeric input only. Example: 1, 10, 100, etc.")
    print(data)

if __name__ == '__main__':
    main()
