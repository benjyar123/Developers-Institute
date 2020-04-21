def encrypt(string):
    message = ""
    for letters in string:
        new = chr(ord(letters) + 14)
        message += str(new)
    print(message)

def decrypt(string):
    message = ""
    for letters in string:
        new = chr(ord(letters) - 14)
        message += str(new)
    print(message)

quit = False
while quit == False:
    function = input("Select function 'encrypt'/'decrypt'/'quit': ")
    if function == "quit":
        break
    text = input("Type the message you would like to encrypt: ")

    if function == "encrypt":
        encrypt(text)
    elif function == "decrypt":
        decrypt(text)



