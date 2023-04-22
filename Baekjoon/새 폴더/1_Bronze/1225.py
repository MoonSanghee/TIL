a, b = input().split()
# 두 수를 각각 문자열로 받아줍니다.
a, b = list(map(int, a)), list(map(int, b))
# 두 수를 각 자리수를 나누어 정수로 변환한수 리스트에 담아줍니다.
print(sum(a) * sum(b))
# 모든 자리수를 더한 다음 두 수를 곱하여줍니다.