

def encrypt ():
    message = input("Enter your message to reverse cipherer : ")
    translated = ''
    i = len(message) - 1

    while i >= 0:
        translated = translated + message[i]
        i = i - 1
    print("Your encrypted message : ", translated)

encrypt()

