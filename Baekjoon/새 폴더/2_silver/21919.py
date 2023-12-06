n = int(input())
# 수의 개수를 받아줍니다.
numbers = list(set(list(map(int, input().split()))))
# 소수의 공배수를 구할것이므로 set함수를 이용하여 중복된 값을 걸러줍니다. 
isPrime = [False] * len(numbers)
# numbers의 길이와 같은 소수인지 표시할 리스트를 만들어줍니다.
for i in range(len(numbers)):
    ok = True
    for j in range(2, numbers[i]):
        if j ** 2 > numbers[i]:
            break
        if numbers[i] % j == 0:
            ok = False
            break
    if ok:
        isPrime[i] = True
    # 소수인지 확인하여 isPrime 리스트에 표시해줍니다.

result = 1
for i in range(len(numbers)):
    if isPrime[i]:
        result *= numbers[i]
# 소수가 있다면 result에 값을 곱해줍니다.

if result == 1:
    print(-1)
else:
    print(result)
# result에 곱해집 값이 없다면 -1을 출력하고 아니면 계산 결과값을 출력해줍니다.