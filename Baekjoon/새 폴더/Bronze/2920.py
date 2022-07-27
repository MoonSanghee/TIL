a = [1, 2, 3, 4, 5, 6, 7, 8]

ascending = []
for i in range(8):
    ascending.append(a[i::] + a[:i:])

b = a[::-1]
descending = []
for i in range(8):
    descending.append(b[i::] + b[:i:])


code = list(map(int, input().split()))
if code in ascending:
    print('ascending')
elif code in descending:
    print('descending')
else:
    print('mixed ')