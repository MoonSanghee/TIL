n = int(input())
name = input()
result = 0
# 주어지는 이름의 길이와 이름을 받고 결과를 담을 변수를 설정해줍니다
for i in name:
    result += ord(i) - 64
# 이름을 순회하며 점수를 구해 결과에 더해줍니다
print(result)
# 결과를 출력해줍니다