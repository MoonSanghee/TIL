n = int(input())
hob = 0
s = n
e = n
cnt = 0
while e > 0:
    hob += e
    if hob == n:
        cnt += 1
    elif hob > n:
        hob -= s
        s -= 1
    e -= 1
print(cnt)
