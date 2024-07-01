j, n = map(int, input().split())
# 목표로하는 크기와 단어가 몇개인지 받아줍니다.
result = 0
# 풀만한 문제의 수를 담을 변수를 만들어줍니다.
for _ in range(n):
    cnt = 0
    for i in input():
        if i == ' ':
            cnt += 1
        elif i in '12345678890':
            cnt += 2
        elif i.islower():
            cnt += 2
        else:
            cnt += 4
        # 입력받은 문제를 순회하며영역의 크기를 받아줍니다.
    if cnt <= j:
        result += 1
        # 목표 크기이하라면 result 값을 1증가시킵니다.

print(result)
# 결과를 출력해줍니다.