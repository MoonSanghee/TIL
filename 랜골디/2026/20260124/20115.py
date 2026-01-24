n = int(input())
drinks = list(map(int, input().split()))
# 주어지는 음료의 수와 음료의 정보들을 받아줍니다
base = max(drinks)
get = (sum(drinks) - base) / 2
# 섞은 음료를 다시 부으면 한번 손실이 일어난 음료가 또다시 손실이 발생하므로 가장 많은 음료에 다른 음료를 모두 한 번씩 붓는것이 손실을 최소화할 수 있습니다
print(base + get)
# 결과를 출력해줍니다