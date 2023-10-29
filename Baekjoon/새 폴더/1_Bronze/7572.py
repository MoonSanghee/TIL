n = int(input())
# 간지를 확인할 연도를 받아줍니다.
word = 'ABCDEFGHIJKL'
base = n - 2013
# 2013년이 "F9"이라고 주어졌으니 2013을 뺀 값을 기준으로 잡아줍니다.
print(word[(base + 5) % 12] + str((base - 1) % 10))
# 간지를 구하여 출력해줍니다.