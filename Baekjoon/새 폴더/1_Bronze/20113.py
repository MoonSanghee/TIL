n = int(input())
votes = list(map(int, input().split()))
cnt = [0] * (n + 1)
# 게임에 참여한 사람의 수와 투표를 받고 각 득표를 담을 리스트를 만들어줍니다
for i in votes:
    if i == 0:
        continue
    cnt[i] += 1
    # 0이라면 무효표이므로 넘기고 아니면 득표를 표시해줍니다

if cnt.count(max(cnt)) == 1:
    print(cnt.index(max(cnt)))
else:
    print("skipped")
    # 최고 득표자가 1명이라면 누구인지 출력하고 아니면 skipped을 출력해줍니다