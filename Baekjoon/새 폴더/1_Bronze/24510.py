n = int(input())
result = 0
# 코드가 몇줄 주어지는지 받고 결과를 담을 변수를 설정해줍니다
for _ in range(n):
    code = input()
    cnt = 0
    cnt += code.count("for")
    cnt += code.count("while")
    # 코드를 받고 for와 while이 몇개씩 들어있는지 확인해줍니다.
    result = max(result, cnt)
    # result값을 갱신해줍니다

print(result)
# result에 담긴 값을 출력해줍니다