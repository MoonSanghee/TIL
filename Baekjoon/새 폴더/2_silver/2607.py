n = int(input())
# 주어지는 단어의 개수를 받아줍니다
base = list(input())
d = dict()
for i in base:
    d[i] = d.get(i, 0) + 1
# 기준이 되는 문자를 받아 각 문자 몇개씩 이루어졌는지 담아줍니다
cnt = 0
# 비슷한 단어의 수를 담을 변수를 설정해줍니다
for _ in range(n - 1):
    word = list(input())
    check = dict()
    for i in word:
        check[i] = check.get(i, 0) + 1
    # 주어지는 단어를 받고 단어의 구성을 딕셔너리에 담아줍니다
    total = 0
    for i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        total += abs(d.get(i, 0) - check.get(i, 0))
    # 알파벳을 차례로 순회하며 각 단어를 이루고 있는 문자의 구성이 얼마나 다른지 변수에 담아줍니다
    if total < 2 or (total == 2 and len(word) == len(base)):
        cnt += 1
    # 다른 문자의 개수가 0개이면 같은 단어이거나 배치만 바꾸면 되고
    # 1개라면 특정한 단어를 1개 더하거나 빼주면 됩니다
    # 2개라면 1개의 문자를 바꾸어 비슷한 단어로 만들수 있는지 확인하여 비슷한 문자의 개수를 갱신해줍니다
print(cnt)
# 비슷한 문자의 수를 출력해줍니다