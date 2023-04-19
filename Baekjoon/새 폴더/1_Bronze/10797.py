n = int(input())%10
# 입력받은 날자를 10으로 나누어 쉬어야하는 차 번호를 찾아줍니다.
numbers = list(map(int, input().split()))
# 차량번호를 리스트로 받아줍니다.
cnt = numbers.count(n)
# count 함수를 이용하여 numbers에 쉬어야하는 차 번호가 몇개 있는지 확인해줍니다.
print(cnt)
# 찾은 값을 출력해줍니다.