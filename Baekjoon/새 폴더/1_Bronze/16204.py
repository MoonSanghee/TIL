n, m, k = map(int, input().split())
print(min(m, k) + min(n - m, n - k))
# 주어지는 변수들을 받아줍니다
# 만들수 있는 앞 뒤면이 같은 카드의 최대 개수를 출력해줍니다