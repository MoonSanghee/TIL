a = int(input())
b = int(input())
c = int(input())
# 주어지는 세 수를 받아줍니다
number = str(a * b * c)
# 세 수를 곱하고 문자열 형태로 변환해줍니다
result = []

for i in range(10):
    result.append(number.count(str(i)))
# 0부터 9 까지 몇개씩 사용되었는지 확인해 결과 리스트에 담아줍니다
for i in result:
    print(i)
    # 차례대로 몇개씩 가지고있는지 출력해줍니다