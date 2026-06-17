T = int(input())
# 테스트케이스의 수를 받아줍니다
for t in range(T):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    # 주어지는 변수들을 받고 사탕 주머니를 오름차순으로 정렬해줍니다
    result = a[-1]
    # 가장 많은 사탕의 값으로 결과를 설정해줍니다
    for i in range(n - m + 1):
        check = a[i: i + m]
        result = min(result, check[-1] - check[0])
    # m개의 연속한 주머니를 확인하며 최대 사탕과 최소 사탕의 개수 차이를 확인하여 결과를 갱신해줍니다
    print(f'#{t + 1} {result}')
    # 결과를 주어진 양식에 맞게 출력해줍니다