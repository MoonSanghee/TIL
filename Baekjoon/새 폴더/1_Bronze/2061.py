k, l = map(int, input().split())
# 두 정수를 받아줍니다
for i in range(2, l):
    if k % i == 0:
        print("BAD", i)
        break
    # l보다 작은 k의 약수가있다면 BAD와 약수를 출력하고
else:
    print("GOOD")
    # 없다면 GOOD을 출력해줍니다