T = int(input())
length = [1, 1, 1, 2, 2]
while len(length) < 100:
    length.append(length[-1] + length[-5])
# 테스트케이스의 개수를 받고 주어진 범위안의 삼각형 변의 길이를 모두 구하여줍니다
for t in range(T):
    n = int(input())
    print(f'#{t + 1} {length[n - 1]}')
    # 삼각형의 차례를 받아 변의 길이를 주어진 양식에 맞게 출력해줍니다