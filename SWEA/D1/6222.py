alphabet = input()

if alphabet.isupper() :
    change = alphabet.lower()
    print('%s(ASCII: %d) => %s(ASCII: %d)'%(alphabet, ord(alphabet), change, ord(change)))
elif alphabet.islower() :
    change = alphabet.upper()
    print('%s(ASCII: %d) => %s(ASCII: %d)'%(alphabet, ord(alphabet), change, ord(change)))
else :
    print(alphabet)