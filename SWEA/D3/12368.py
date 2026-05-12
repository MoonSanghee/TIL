tc = int(input())
# 테스트 케이스가 몇개인지 받아줍니다
for t in range(tc):
    A, B = map(int, input().split())
    # 현재시간과 몇 시간 후를 확인할지를 받아줍니다
    print(f'#{t + 1} {(A + B) % 24}')
    # 시계가 나타내는 시간을 주어진 양식대로 출력해줍니다