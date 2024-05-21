primes = []
# 소수를 담을 리스트를 만들어줍니다.
num = 2
while True:
    if num == 103:
        break
    for i in range(2, num):
        if num % i == 0:
            break
    else:
        primes.append(num)
    num += 1
# 101과 103을 곱하면 10000을 넘으므로 103이하의 소수를 구하여 리스트에 담아줍니다.

n = int(input())
# 주어지는 수를 받아줍니다.
idx = 0
while True:
    answer =  primes[idx] * primes[idx + 1] 
    if answer > n:
        print(answer)
        break
    idx += 1
    # 주어진 수보다 큰 특별한 수를 찾아 출력해줍니다.