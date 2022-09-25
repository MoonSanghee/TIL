n = list(input())
for i in range(len(n)):
    p = i
    for j in range(i + 1, len(n)):
        if num < int(n[j]):
            num = int(n[j])
            p = j
    if n[p] != n[i]:
        n[i], n[p] = n[p], n[i]
print(''.join(n))