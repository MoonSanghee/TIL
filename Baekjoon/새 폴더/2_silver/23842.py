number = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]
n = int(input())
# 만드려는 숫자별 필요한 성냥의 개수를 리스트에 담고 주어지는 성냥의 수를 받아줍니다
for i in range(100):
    for j in range(100):
        if i + j >= 100:
            continue
        # 100 이하 두 수의 조합을 순회하며 합이 세자리수라면 확인할 필요가 없습니다
        cost = number[i // 10] + number[i % 10] + number[j // 10] + number[j % 10] + number[(i + j) // 10] + number[(i + j) % 10] + 4
        # 식을 만드는데 필요한 성냥의 개수를 확인해줍니다
        if cost == n:
            print(f"{i:02d}+{j:02d}={(i + j):02d}")
            exit()
            # 주어진 성냥을 다 사용하는 식이 만들어준다면 출력을하고 작동을 멈추어줍니다

print("impossible")
# 반복을 진행하며 멈추지 않았다면 성냥을 모두 쓰는 코드가 없는 경우이므로 불가능을 출력해줍니다