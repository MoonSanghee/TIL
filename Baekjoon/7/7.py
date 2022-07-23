# 7-7 문제번호 2839

n = int(input())
n5 = n // 5
b = []
for i in range(n5 + 1):
    a = (n - i * 5) // 3    
    if ((n - i * 5) % 3) == 0:
        b.append(a + i)
if len(b) == 0:
    print(-1)
else:    
    print(min(b))
