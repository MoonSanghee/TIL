A, B, C = map(int, input().split())
# 주어지는 변수들을 받아줍니다
for _ in range(C % 2):
    A ^= B
# 연산을 실행해줍니다
print(A)
# 결과를 출력해줍니다