n = int(input())
# 파일의 개수를 받아줍니다.
numbers = list(map(int, input().split()))
# 파일을 리스트에 받아줍니다.
limited = int(input())
# 최대로 받을수 있는 용량을 받아줍니다
total = 0
# 총 용량을 담을 변수를 정해줍니다.
for number in numbers:
    total += (number // limited) * limited
    if number % limited:
        total += limited
    # 수를 순회하며 필요한 용량을 total에 더해줍니다.
print(total)
# total의 값을 출력해줍니다.