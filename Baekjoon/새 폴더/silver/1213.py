alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
al = []
sen = input().strip()
cnt = 0
hol = ''
for i in range(26):
    ac = sen.count(alpha[i])
    if ac % 2 != 0:
        cnt += 1
        hol += alpha[i]
    al.append(ac//2)
if cnt > 1:
    print("I'm Sorry Hansoo")
else:
    result = ''
    for i in range(26):
        result += alpha[i] * al[i]
    result = result + hol + result[::-1]
    print(result)