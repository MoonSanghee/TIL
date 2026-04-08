alpa = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
T = int(input())
# 입력이 몇개 주어지는지 받아줍니다
d = dict()
for i in range(26):
    d[i] = alpa[i]
    d[alpa[i]] = i
# 딕셔너리에 알파벳의 순서를 (키, 밸류), (밸류, 키)로 묶어 넣어줍니다
for _ in range(T):
    n, start = input().split()
    n = int(n)
    start = d[start]
    # 삼각형의 크기와 맨 윗줄의 알파벳을 받아줍니다
    for i in range(n):
        i += 1
        print(d[start] * i)
        start = (start + 1) % 26
    print()
    # 주어진 형식에 맞게 삼각형을 출력해줍니다