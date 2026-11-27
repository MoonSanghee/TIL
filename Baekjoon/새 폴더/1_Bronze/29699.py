word = 'WelcomeToSMUPC'

n = int(input()) - 1

n %= len(word)

print(word[n])