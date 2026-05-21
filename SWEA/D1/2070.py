T = int(input())
# 테스트 케이스의 수를 받아줍니다
for t in range(T):
    l, r = map(int, input().split())
    # 주어지는 두 수를 받아줍니다
    if l > r:
        print(f'#{t + 1} >')
    elif l == r:
        print(f'#{t + 1} =')
    else:
        print(f'#{t + 1} <')
    # 두 수를 비교한 결과를 주어진 양식에 맞게 출력해줍니다