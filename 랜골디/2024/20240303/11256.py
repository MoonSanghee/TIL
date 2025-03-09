t = int(input())
# 테스트 케이스의 개수를 받아줍니다.
for _ in range(t):
    j, n = map(int, input().split())
    items = []
    # 상자의 개수와 사탕의 개수를 받고 상자의 크기를 담을 변수를 리스트형태로 설정해줍니다.

    for _ in range(n):
        c, r = map(int, input().split())
        item = c * r
        items.append(item)
        # 상자의 가로와 세로 크기를 받아 면적을 구한 후 items에 넣어줍니다.
    
    items.sort()
    # 상자들을 넓이를 기준으로 오름차순 정렬을 실행해줍니다.
    
    cnt = 0
    while j > 0:
        size = items.pop()
        cnt += 1
        j -= size
        # 사탕이 다 담길때까지 큰 상자부터 꺼내 사탕을 담으며 몇 개의 박스가 필요한지 확인해줍니다.
    
    print(cnt)
    # 필요한 상자의 개수를 출력해줍니다.