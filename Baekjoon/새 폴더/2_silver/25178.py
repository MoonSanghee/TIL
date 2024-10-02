n = int(input())
word1 = input()
word2 = input()
# 단어의 길이와 두 단어를 받아줍니다
first, second, third = False, False, False
# 주어진 세 조건을 통과하는지 확인하여 상태를 담을 변수를 설정해줍니다.
if sorted(word1) == sorted(word2):
    first = True
# 각 단어를 정렬해서 비교하면 각 단어를 재배열하여 같은 단어로 만들수있으므로 첫 조건을 확인할수있습니다.

if word1[0] == word2[0] and word1[-1] == word2[-1]:
    second = True
# 각 단어의 첫 문자와 마지막 문자를 비교하여 두번째 조건을 확인해줍니다.

for i in 'aeiou':
    word1 = word1.replace(i, '')
    word2 = word2.replace(i, '')
# 모음을 차례대로 제거하여 단어를 갱신해줍니다.
if word1 == word2:
    third = True
# 모음을 제거한 단어를 비교하여 세번째 조건을 확인해줍니다.
if first and second and third:
    print('YES')
else:
    print('NO')
# 조건을 모두 통과하는지 출력해줍니다.