# n, m = map(int,input().split())
# a = list(map(int, input().split()))
# b = list(map(int, input().split()))
# for i in range(m):
#     a.append(b[i])
# a.sort()
# print(*a)

# 투 포인트 이용한 풀이
n,m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a.sort()
b.sort()
s1 = 0
s2 = 0
c = []
while len(c) < n + m:
    i = a[s1]
    j = b[s2]
    if i > j:
        c.append(j)
        s2 += 1
        if s2 == m:
            b[-1] = 1000000001
            s2 -= 1
    else:
        c.append(i)
        s1 += 1
        if s1 == n:
            a[-1] = 1000000001
            s1 -= 1
print(*c)