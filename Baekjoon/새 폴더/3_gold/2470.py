n = int(input())
li = list(map(int, input().split()))
li.sort()
s = 0 
e = n - 1
mini = 2000000000
# 10억 이하의 서로 다른 수들이라 하였으므로 두 수를 합한 값이 20억을 넘을수 없으니 시작 비교값을 20억으로 잡아주었습니다.
minip = []
while s < e:
    if abs(li[s] + li[e]) < mini:
        mini = abs(li[s] + li[e])
        minip = [li[s], li[e]]
    if li[s] + li[e] > 0:
        e -= 1
    else:
        s += 1
print(*minip)
# 투포인트를 이용하여 두 수를 합한 절대값이 가장 작은 경우를 찾고 그 둘이 무엇인지 출력해주었습니다.