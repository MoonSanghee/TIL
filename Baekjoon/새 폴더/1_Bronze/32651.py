multiples = []
number = 2024
# 배수를 담을 리스트와 수를 설정해줍니다
while number <= 100000:
    multiples.append(number)
    number += 2024
# 주어진 범위 아래의 모든 배수를 리스트에 담아줍니다
if int(input()) in multiples:
    print("Yes")
else:
    print("No")
# 주어진 수가 외우고있는 수인지 확인하여 결과를 출력해줍니다