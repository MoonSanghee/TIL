a, d, k = map(int, input().split())
# 주어지는 세 정수를 받아줍니다
if (k - a) % d == 0 and (k-a)//d >= 0:
    print(((k - a) // d) + 1)
else:
    print('X')
# 주어진 k가 등차수열에 포함되는지 확인하고 결과를 출력해줍니다