n = int(input())
ingredients = [list(map(int, input().split())) for _ in range(n)]
# 재료의 개수와 재료가 내는 맛을 받아줍니다.
result = 1e9
# 결과를 담을 변수를 설정해줍니다.
def mix(depth, cnt, sour, bitter):
    # 깊이, 섞은 재료의 수, 신맛, 쓴맛을 받아줍니다.
    global result
    if cnt != 0:
        if abs(sour - bitter) < result:
            result = abs(sour - bitter)
        # 하나 이상의 재료를 섞었을때 결과 값이 더 좋아진다면 값을 갱신해줍니다.
    if depth == n:
        return
    # depth가 n에 도달하여 모든 경우를 탐방하였다면 연산을 멈추어줍니다.
    mix(depth + 1, cnt + 1, sour * ingredients[depth][0], bitter + ingredients[depth][1])
    mix(depth + 1, cnt, sour, bitter)
    # 각 재료를 넣거나 넣지 않는 형태로 재귀를 실행해줍니다.

mix(0, 0, 1, 0)
# depth, cnt는 0에서 시작하고 쓴맛은 합 연산이기때문에 0 신맛은 곱연산이기때문에 1로 시작해줍니다.
print(result)
# result에 담긴 값을 출력해줍니다.