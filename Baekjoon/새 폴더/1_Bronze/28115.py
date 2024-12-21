n = int(input())
# 주어지는 수열의 길이를 확인해줍니다
numbers = list(map(int, input().split()))
B = [numbers[0] * 2]
C = [numbers[0] * -1]
# 수열을 받고 B와 C열 리스트를 만들어 주어진 수열의 첫 값에서 각 2와 -1을 곱한값을 넣어줍니다
if n == 1:
    print("YES")
    print(3)
    print(numbers[0] - 3)
elif n == 2:
    B.append(numbers[1] * 2)
    C.append(numbers[1] * -1)
    print("YES")
    print(*B)
    print(*C)
# 수열의 길이가 2이하라면 무조건 등차수열이 성립하므로 형식에 맞추어 값을 출력해줍니다
elif n > 2:
    check = numbers[1] - numbers[0]
    for i in range(1, n):
        B.append(numbers[i] * 2)
        C.append(numbers[i] * -1)
        if numbers[i] - numbers[i - 1] != check:
            print("NO")
            break
    else:
        print("YES")
        print(*B)
        print(*C)
    # 수열의 길이가 3이상이라면 등차수열인지 확인하여 알맞은 형태로 결과를 출력해줍니다