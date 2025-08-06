import sys
input = sys.stdin.readline

n = int(input())
arr = [tuple(input().split()) for _ in range(n)]
# 주어지는 쌍의 수를 받고 리스트에 튜플로 묶어 담아줍니다
arr.sort(key=lambda x: x[1], reverse=True)
arr.sort(key=lambda x: x[0])
# 멘티를 기준으로 사전 역순으로 정렬한 다음 멘토를 기준으로 사전순 정렬을 한 번 더 해줍니다
for mentor, mentee in arr:
    print(mentor, mentee)
    # 멘토와 멘티의 쌍을 차례대로 출력해줍니다