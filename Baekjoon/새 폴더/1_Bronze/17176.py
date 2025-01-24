n = int(input())
numbers = list(map(int, input().split()))
base = ' ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
# 주어지는 문자의 개수와 문자를 받고 문자에 매칭되는 번호대로 기본을 설정해줍니다
word = input()
d = {}

for i in word:
    d[i] = d.get(i, 0) + 1
# 주어지는 문장을 받고 각 문자가 몇개씩 필요한지 받아줍니다
for i in numbers:
    if base[i] in d and d[base[i]] > 0:
        d[base[i]] -= 1
# 주어지는 문자가 문장에 있는지 확인하여 더 필요한 문자가 없을때까지 값을 갱신해줍니다
for i in d:
    if d[i] > 0:
        print('n')
        break
else:
    print('y')
# 충분히 문자가 주어졌는지 확인해 결과를 출력해줍니다