n = int(input())
s = input()
d = dict()
# 주어지는 변수들을 받고 각 문자의 개수를 담을 딕셔너리를 만들어줍니다
for i in s:
    d[i] = d.get(i, 0) + 1
# 각 문자의 개수를 확인해줍니다
if len(d) != 4:
    print(0)
    # 모든 문자가 존재하는것이 아니라면 0을 출력해줍니다
else:
    result = 1
    for i in d:
        result *= d[i]
    print(result % 1000000007)
    # 모든 문자의 개수를 곱하여 주어진 수를 나눈 나머지를 출력해줍니다