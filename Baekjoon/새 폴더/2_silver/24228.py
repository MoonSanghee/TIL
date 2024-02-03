n, r = list(map(int, input().split()))
# 젓가락의 종류와 몇 짝을 만들지 받아줍니다.
one = n + 1
# 첫 한 쌍을 만드는데 n + 1번의 뽑기가 필요합니다
others = 2 * (r - 1)
# 나머지 r - 1쌍을 뽑기 위해는 2 * (r - 1)번의 뽑기가 필요합니다.
print(one + others)
# 둘을 합친 뽑기수를 출력해줍니다.