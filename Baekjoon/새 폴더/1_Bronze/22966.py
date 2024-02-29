n = int(input())
questions = []
# 문제의 개수와 문제를 담을 리스트를 만들어줍니다.
for _ in range(n):
    problem, level = input().split()
    level = int(level)
    # 문제와 난이도를 받고 난이도는 정수형으로 바꾸어줍니다.
    questions.append((level, problem))
    # 난이도와 문제의 튜플 형태로 questions에 담아줍니다.

questions.sort(key = lambda x : x[0])
print(questions[0][1])
# 난이도 순으로 오름차순 정렬하여 가장 앞의 문제를 출력해줍니다.