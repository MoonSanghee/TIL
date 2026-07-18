T = int(input())
# 테스트케이스의 개수를 받아줍니다
def search(pages, target):
    cnt = 1
    start = 1
    end = pages

    while (start + end) // 2 != target:
        center = (start + end) // 2
        cnt += 1
        if target > center:
            start = center
        else:
            end = center

    return cnt
# 이분탐색 과정이 몇번 진행되는지 찾을 함수를 설정해줍니다
for t in range(T):
    P, A, B = map(int, input().split())
    # 주어지는 변수들을 받아줍니다
    a = search(P, A)
    b = search(P, B)
    # 두 수를 찾아줍니다
    if a < b:
        winner = 'A'
    elif a > b:
        winner = 'B'
    else:
        winner = '0'
    # 승자를 확인해줍니다
    print(f'#{t + 1} {winner}')
    # 결과를 주어진 양식에 맞춰 출력해줍니다