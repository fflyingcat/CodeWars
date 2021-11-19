def rot13(message):
    encrypted_message = ""
    for i in range(len(message)):
        char = ord(message[i])
        if ((char >= 65 and char <= 90) or (char >=97 and char <= 122)):
            if (char <= 77 or (char > 90 and char <= 109)):
                encrypted_message += chr(char+13)
            else:
                encrypted_message += chr(char - 13)
        else:
            encrypted_message += chr(char)
    return encrypted_message
#https://www.codewars.com/kata/52223df9e8f98c7aa7000062
