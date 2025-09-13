n = int(input())
problems = [int(input()) for _ in range(n)]
# 문제의 개수와 주어지는 문제의 난이도를 받아줍니다
if problems[0] == min(problems):
    print("ez")
elif problems[0] == max(problems):
    print("hard")
else:
    print("?")
# 첫 문제의 난이도에 대하여 결과를 출력해줍니다