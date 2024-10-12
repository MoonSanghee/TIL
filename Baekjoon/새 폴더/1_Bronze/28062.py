n = int(input())
candy = list(map(int, input().split()))
candy.sort()
# 사탕의 개수와 사탕을 받고 오름차순으로 정렬해줍니다
result = sum(candy)
# 사탕 개수의 합을 구해줍니다
if result % 2 == 1:
    # 사탕의 합이 홀수라면
    for i in candy:
        if i % 2 == 1:
            result -= i
            break
    # 가장 작은 홀수개만큼 빼줍니다.
print(result)
# 결과를 출력해줍니다.