n, m = map(int, input().split())

balls = [i for i in range(n + 1)]
# 공의 개수와 자리 바꿀 횟수를 입력받고 각 번호를 가지는 볼을 리스트로 만들어줍니다.

for _ in range(m):
    b1, b2 = map(int, input().split())
    balls[b1],balls[b2] = balls[b2], balls[b1]
# 공을 바꾸는 횟수만큼 두 공의 번호를 입력받아 값을 바꾸어줍니다.

print(*balls[1:])
# 위치를 다 바꾼 다음 리스트에서 1번 인덱스부터 값을 확인하여 안의 값을 출력해줍니다.