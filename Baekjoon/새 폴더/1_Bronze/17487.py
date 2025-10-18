S = input()
# 주어지는 입력을 받아줍니다
left = 'qwertyasdfgzxcvb'
right = 'uiophjklnm'
# 각 손으로 누르는 문자를 담아줍니다
cnt = [0, 0, 0]
# 버튼을 누르는 횟수를 담을 변수를 설정해줍니다
for i in S:
    if i.isupper():
        cnt[2] += 1
        i = i.lower()
    # 입력의 문자를 순회하면 대문자라면 어느 손으로든 누를수 있습니다
    if i in left:
        cnt[0] += 1
    elif i in right:
        cnt[1] += 1
    else:
        cnt[2] += 1
    # 문자를 어떤 손으로 누르는지 확인해줍니다

while cnt[2]:
    cnt[2] -= 1
    if cnt[0] <= cnt[1]:
        cnt[0] += 1
    else:
        cnt[1] += 1
# 차이를 최소화해줍니다
print(cnt[0], cnt[1])
# 각 손으로 누르는 횟수를 출력해줍니다