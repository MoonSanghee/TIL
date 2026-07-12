n = int(input())
# 주어지는 수를 받아줍니다
result = []
# 결과를 담을 변수를 설정해줍니다
for i in range(1, n + 1):
    number = str(i)
    cnt = -1
    if '3' in number or '6' in number or '9' in number:
        cnt = 0
    # 주어진 수 이하의 정수를 순회하며 3, 6, 9가 포함되어있는지 확인해줍니다
    if cnt == 0:
        for j in number:
            if j in '369':
                cnt += 1
    # 3, 6, 9중에 하나라도 존재한다면 개수를 확인해줍니다
    if cnt == -1:
        result.append(number)
    else:
        result.append('-' * cnt)
    # 결과에 값을 추가해줍니다
print(*result)
# 결과를 출력해줍니다