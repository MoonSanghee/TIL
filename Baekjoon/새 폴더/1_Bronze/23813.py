n = input()
# 최초 주어지는 수를 받아줍니다.
result = 0
# 결과를 담을 변수를 설정해줍니다.
for i in range(len(n)):
    result += int(n[i:] + n[:i])
    # 수를 회전시키며 나온 값을 결과에 더해줍니다.

print(result)
# 결과를 출력해줍니다.