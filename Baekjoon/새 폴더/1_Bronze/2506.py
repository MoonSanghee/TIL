n = int(input())
# 문제의 개수를 받아줍니다.
result = 0
# 최종 점수가 들어갈 변수를 지정해줍니다.
straight = 0
# 연속해서 몇개의 문제가 맞았는지 저장해줄 변수를 지정해줍니다.
test = list(map(int, input().split()))
# 체점 결과를 받아줍니다.
for i in test:
    # 체점 결과를 순회하며
    if i == 1:
        straight += 1
        # 맞췄다면 연속하여 맞은 것을 1 더해주고
    else:
        straight = 0
        # 틀렸다면 연속한 정답을 0으로 바꾸어줍니다.
    result += straight
    # 결과에 연속해서 맞은 정답을 더해줍니다.

print(result)
# 최종 점수를 출력해줍니다.