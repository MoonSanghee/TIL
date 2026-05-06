n = int(input())
# 테스트 케이스의 개수를 받아줍니다
for _ in range(n):
    directions = set(input())
    # 주어지는 이동 방향을 받아줍니다
    if 'N' in directions and 'S' not in directions:
        print('No')
    elif 'E' in directions and 'W' not in directions:
        print('No')
    elif 'W' in directions and 'E' not in directions:
        print('No')
    elif 'S' in directions and 'N' not in directions:
        print('No')
    else:
        print('Yes')
    # 집으로 돌아갈 수 있는지 확인하여 결과를 출력해줍니다