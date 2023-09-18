t = int(input())
for _ in range(t):
    v, e = map(int, input().split())
    # 꼭지점과 모서리의 수를 받아줍니다.
    print(e + 2 - v)
    # 모서리의 수에 2를 더하고 꼭지점의 수를 뺀 값을 출력해줍니다.