n = int(input())
marbles = list(map(int, input().split()))
result = 0
# 수열의 길이와 수열, 최대값을 담을 변수를 정해줍니다.
def back(num):
    global result
    if len(marbles) == 2:
        result = max(result, num)
        # 처음과 끝 수만 남았다면 수열과 비교하여 값을 갱신해줍니다.
    for i in range(1, len(marbles) - 1):
        get = marbles[i - 1] * marbles[i + 1]
        # 각 자리에서 얻는 값을 구하여줍니다.
        value = marbles.pop(i)
        # i번 수를 빼서 value로 받아줍니다.
        back(num + get)
        # 재귀를 실행하고
        marbles.insert(i, value)
        # 뺀 값을 리스트에 다시 담아줍니다.

back(0)
# 시작값을 0으로 연산을 실행해줍니다.
print(result)
# result에 담긴 값을 출력해줍니다.