n, m = map(int, input().split())
# 키보드의 수와 입력의 수를 받아줍니다.
result = ''
push = []
# 입력을 담을 변수와 결과를 담을 변수를 만들어줍니다.
for _ in range(m):
    a, b, c = input().split()
    a = int(a)
    b = int(b)
    push.append((a, b, c))
    # 키보드 번호와 입력 시간 입력 문자를 받아줍니다.

push.sort(key = lambda x : [x[1], x[0]])
# lambda함수를 이용해 입력 시간과 키보드 번호 순으로 정렬해줍니다.
for a, b, c in push:
    result += c
# 입력 문자를 차례대로 더해 단어를 만들어줍니다.
print(result)
# 입력한 단어를 출력해줍니다.