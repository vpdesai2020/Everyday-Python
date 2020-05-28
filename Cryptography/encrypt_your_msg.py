source='abcdefghijklmnopqrstuvwxyz'
key=7
encrypted=''
message=input("Enther the message")

for character in message:
    position=source.find(character)
    newposition=(position+key)%26
    encryptchar=source[newposition]
    encrypted += encriptchar

print("Here is your Encripted Message: ", encrypted)
