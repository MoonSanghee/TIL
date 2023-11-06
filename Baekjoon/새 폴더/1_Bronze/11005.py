n, b = map(int, input().split())
# 10진법 수와 몇 진법으로 변환할지를 받아줍니다.
d = dict()
num = 0
for letter in "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ":
    d[num] = letter
    num += 1
# 36까지 어떤 문자로 매칭되는지 받아줍니다.
result = []

while n:
    result.append(d[n % b])
    n //= b
    # 변환하였을 때 뒤의 자리부터 구하여줍니다.
print(''.join(result[::-1]))
# 리스트를 뒤집어 join 함수를 이용하여 묶은 값을 출력해줍니다.