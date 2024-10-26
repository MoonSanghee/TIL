n = int(input())
# 전투의 수를 받아줍니다.
for i in range(n):
    Good = list(map(int, input().split()))
    Evil = list(map(int, input().split()))
    # 두 진영의 상황을 받아줍니다.
    result = 0

    result += Good[0] + Good[1] * 2 + Good[2] * 3 + Good[3] * 3 + Good[4] * 4 + Good[5] * 10
    result -= Evil[0] + Evil[1] * 2 + Evil[2] * 2 + Evil[3] * 2 + Evil[4] * 3 + Evil[5] *5 + Evil[6] * 10
    # 주어지는 점수를 계산해줍니다.
    if result > 0:
        print(f"Battle {i + 1}: Good triumphs over Evil")
    elif result < 0:
        print(f"Battle {i + 1}: Evil eradicates all trace of Good")
    else:
        print(f"Battle {i + 1}: No victor on this battle field")
    # 결과에 따라 주어진 양식에 맞추어 출력해줍니다.