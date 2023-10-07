n = int(input())
# 문자열의 개수를 받아줍니다.
points = dict()
# 각 문자의 포인트를 저장할 딕셔너리를 만들어줍니다.
point = 65
# 65점부터 1씩 증가하므로 65로 시작하여줍니다.
total = 0
# 전체 점수를 저장할 변수를 만들어줍니다.
for letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
    points[letter] = point
    total += point
    point += 1
    # 각 문자의 점수를 매칭하여 딕셔너리로 저장해줍니다.
    # 전체 점수도 구해줍니다.

for _ in range(n):
    have = 0
    words = list(set(input()))
    # 중복된 문자를 지우고 리스트로 변환하여줍니다.
    for word in words:
        have += points[word]
        # 가지고 있는 문자들의 점수를 구하여줍니다.
    print(total - have)
    # 전체 점수에서 가지고 있는 점수를 빼줍니다.