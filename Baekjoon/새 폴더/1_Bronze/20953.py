import sys
input = sys.stdin.readline

def dolmen(a, b):
    n = a + b
    return (n * n * (n - 1)) // 2
# 주어진 C코드를 구하는 함수를 만들어줍니다
T = int(input())
# 테스트 케이스의 수를 받아줍니다
for _ in range(T):
    a, b = map(int, input().split())
    print(dolmen(a, b))
    # 주어지는 두 수를 받아 함수를 실행한 결과값을 출력해줍니다