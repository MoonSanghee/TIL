jinho = input()
# 진호의 MBTI를 받아줍니다
result = 0
# 결과를 담을 변수를 받아줍니다
n = int(input())
for _ in range(n):
    friend = input()
    if jinho == friend:
        result += 1
# 친구의 수와 친구들의 MBTI를 받고 진호의 MBTI가 동일한 친구가 나올때마다 결과를 갱신해줍니다
print(result)
# 결과를 출력해줍니다