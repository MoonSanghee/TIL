word = input()
cnt = [0, 0]
# 단어를 받고 JOI와 IOI의 수를 담을 변수를 설정해줍니다.
for i in range(len(word) - 2):
    key = word[i:i + 3]
    if key == 'JOI':
        cnt[0] += 1
    elif key == 'IOI':
        cnt[1] += 1
    # 단어를 순회하며 JOI와 IOI를 찾아 cnt의 각 자리에 값을 추가해줍니다.
for i in cnt:
    print(i)
    # JOI와 IOI의 개수를 출력해줍니다.