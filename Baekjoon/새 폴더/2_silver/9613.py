import math
tc = int(input())

for t in range(tc):
    nums = list(map(int, input().split()))
    result = 0
    for i in range(1, nums[0] + 1):
        for j in range(i + 1, nums[0] + 1):
            result += math.gcd(nums[i], nums[j])
    
    print(result)

# 주어진 숫자들과 그 수 다음부터 끝까지 숫자를 차례로 짝지어주고
# math 라이브러리의 gcd 함수를 이용하면 쉽게 두 수의 최대 공약수를 구할 수 있다.
# 그 값들을 전부 더하면 원하는 결과값을 얻을 수 있다.

t = int(input())

def gcd(a, b):
    if not b:
        return a
    else:
        return gcd(b, a%b)

for t in range(tc):
    nums = list(map(int, input().split()))
    l = nums.pop(0)
    result = 0
    for i in range(l):
        for j in range(i + 1, l):
            result += gcd(nums[i], nums[j])
    print(result)

# 같은 식으로 모든 수들을 짝지어주고 유클리드 호제법을 이용한 최대 공약수를 구하는 함수를
# 정의하여 나오는 최대 공약수들을 다 더해주는 방식으로도 접근 할 수 있다.