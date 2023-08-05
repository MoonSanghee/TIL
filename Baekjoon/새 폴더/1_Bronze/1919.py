word1 = input()
word2 = input()
# 두 단어를 받아줍니다
count = 0
# 바꿔야할 문자의 개수를 저장할 변수를 선언해줍니다.
cnt = dict()
# 어떤 문자를 몇개 바꾸어야하는지 딕셔너리에 저장해줍니다.
for letter in word1:
    # 단어 1의 문자를 순회하며
    if letter in cnt:
        cnt[letter] += 1
        # cnt에 값이 있다면 1을 더하고
    else:
        cnt[letter] = 1
        # 없다면 1로 설정해줍니다.

for letter in word2:
    # 단어 2의 문자를 순회하며
    if letter not in cnt:
        cnt[letter] = -1
        # 문자가 cnt에 없다면 -1로 값을 설정해주고
    else:
        cnt[letter] -= 1
        # 있다면 1을 빼줍니다.

for i in cnt:
    count += abs(cnt[i])
# 딕셔너리에 저장된 문자들을 확인하며 value의 절대값만큼 count에 더해줍니다.
print(count)
# count에 저장된 수를 출력해줍니다.