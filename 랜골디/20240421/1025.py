n, m = map(int, input().split())
maps = [list(input()) for _ in range(n)]
# 표의 크기와 표를 받아줍니다
result = -1
# 결과값을 담을 변수를 설정해줍니다.
     
# 제곱수인지 확인할 함수를 만들어줍니다
def check(number):
    number = int(number)
    if int(number ** 0.5) ** 2 == number:
        return True
    else:
        return False


for i in range(n):
    for j in range(m):
        # 표의 모든 영역에 대하여 수를 선택하므로 모든 영역을 확인해줍니다.
        for dx in range(-n, n):
            for dy in range(-m, m):
                # 두개 이상의 수를 뽑기위해 등차수열의 범위를 설정해줍니다.
                number = ''
                # 수를 뽑아 만들어질 값을 담을 변수를 설정해줍니다.
                x, y = i, j
                # 표의 위치가 이동될것이므로 변형시킬 기본값을 설정해줍니다.
                if dx == 0 and dy == 0:
                    continue
                # dx, dy가 둘 다 0이라면 같은 자리값을 무수히 찍을것이기에 넘겨줍니다.
                while 0 <= x < n and 0 <= y < m:
                    number += maps[x][y]
                    if check(number):
                        result = max(result, int(number))
                    # 수에 표에서 확인한 값을 더해 제곱수인지 확인하고 제곱수라면 result 값과 비교하여 갱신해줍니다.
                    x += dx
                    y += dy
                    # 좌표값을 이동 가능할때까지 반복하여 시행해줍니다.

print(result)
# 결과값을 출력해줍니다.