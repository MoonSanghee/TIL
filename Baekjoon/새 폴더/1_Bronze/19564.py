word = input()
# 단어를 입력받습니다.
cnt = 1
# 입력횟수를 담을 변수를 설정해줍니다.
for i in range(len(word) -  1):
    if ord(word[i]) >= ord(word[i + 1]):
        cnt += 1
    # 각 문자를 확인하며 다음 문자와 같거나 이전 문자가 다음 문자보다 뒤의 문자라면 입력이 한 번 더 필요합니다.

print(cnt)
# 입력 횟수를 출력합니다.