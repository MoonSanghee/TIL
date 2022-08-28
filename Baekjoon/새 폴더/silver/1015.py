n = int(input())
numbers = list(map(int, input().split()))
num = sorted(numbers)
check = dict()
result = []
for i in numbers:
    if i in check:
        check[i] += 1
    else:
        check[i] = 1
    if check[i] != 1:
        result.append(num.index(i) + check[i] - 1)
    else:
        result.append(num.index(i))
print(*result)

# 찾아본 코드
n = int(input())
t = list(map(int, input().split()))
s_li = sorted(t)
li = []
for i in range(n):
    idx = s_li.index(t[i])
    li.append(idx)
    s_li[idx] = -1
print(*li)
# 원래 주어진 리스트에 인덱스 값에 위치한 숫자를 정렬한 인덱스 값에서 찾아주고 사용한
# 값을 -1로 바꾸어 가장 앞으로 보내어 중복된 값이 있으면 인덱스 위치를 밀어주는 효과를 준듯하다.