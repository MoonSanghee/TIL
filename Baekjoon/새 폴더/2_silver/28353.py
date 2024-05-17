n, k = map(int, input().split())
cats = list(map(int, input().split()))
# 고양이가 몇마리인지와 제한 무게를 받고 각 고양이의 무게를 받아줍니다.
cats.sort()
result = 0
# 몇 명이 두 마리의 고양이를 안을수있는지 담을 변수를 설정하고 고양이를 무게별 오름차순으로 정렬해줍니다.
s, e = 0, n - 1
# 가장 앞의 고양이와 가장 뒤의 고양이를 설정해줍니다.
while True:
    if e <= s:
        break
    # 두 인덱스값이 만나면 1마리밖에 안지못하므로 실행을 멈추어줍니다.
    if cats[s] + cats[e] <= k:
        result += 1
        s += 1
        # 두 고양이를 안을수 있는 조합이면 1쌍이 지어졌음을 표시하고 다음으로 가벼운 고양이로 s인덱스를 바꿔줍니다.
    e -= 1
    # 무거운순으로 확인해줍니다

print(result)
# result에 담긴값을 출력해줍니다.