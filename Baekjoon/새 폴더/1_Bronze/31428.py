n = int(input())
friends = list(input().split())
# 친구의 수와 친구들의 신청내용을 받아줍니다
hellobit = input()
result = 0
# 헬로빗의 신청내용을 받고 같은 친구들의 수를 담을 변수를 설정해줍니다
for i in friends:
    if i == hellobit:
        result += 1
# 친구들을 순회하며 확인해줍니다
print(result)
# 결과를 출력해줍니다