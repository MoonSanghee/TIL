n = int(input())
# 주어지는 재료의 수를 받아줍니다
ingredients = list(input().split())
used = list(input().split())
# 필요한 재료와 사용한 재료를 받아줍니다
for i in ingredients:
    if i not in used:
        print(i)
        break
# 사용하지 않은 재료를 찾아 출력해줍니다