n = int(input())

mod = 1000000
fibo = [0, 1]
p = mod//10*15

for i in range(2, p):
    fibo.append(fibo[i - 1]+fibo[i - 2])
    fibo[i] %= mod

print(fibo[n%p])

# 피보나치 수를 K로 나눈 나머지는 항상 주기를 갖게된다는 피사노 주기라는 방법을 사용해야하는 문제였습니다.
# 주기의 길이가 P 일 때, n번째 피보나치 수를 M으로 나눈 나머지는 n%p번째 피보나치 수를
# m을 나눈 나머지와 같습니다.
# m = 10**k 일 때, k > 2라면 주기는 항상 15*10**(k - 1)이라고합니다.