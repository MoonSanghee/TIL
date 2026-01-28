n = int(input())
word = input()
# 주어지는 문자열의 길이와 문자열을 받아줍니다
for i in range(1, n):
    front, back = word[:i], word[n - i:]
    cnt = 0
    # 문자열의 앞부분 단어와 뒷부분 단어를 받고 다른 문자의 개수를 담을 변수를 설정해줍니다
    for j in range(i):
        if front[j] != back[j]:
            cnt += 1
    if cnt == 1:
        print("YES")
        break
    # 문자를 순회하며 다른 문자의 수가 1개이면 비타민 문자열에 해당합니다
else:
    print("NO")
    # 비타민 문자열에 해당하지 않으면 아니라고 출력해줍니다