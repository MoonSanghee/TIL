question, answer = input().split('=')
# 문제와 답 부분을 나눠줍니다
numbers = list(map(int, question.split('+')))
# 문제의 수들을 리스트에 넣어줍니다
if sum(numbers) == int(answer):
    print('YES')
else:
    print('NO')
# 문제를 계산한 값과 결과를 비교하여 정답을 출력해줍니다