a, b = map(str, input().split())

a = a.replace('6', '5')
b = b.replace('6', '5')

little = int(a) + int(b)

a = a.replace('5', '6')
b = b.replace('5', '6')

big = int(a) + int(b)
print(little, big)
