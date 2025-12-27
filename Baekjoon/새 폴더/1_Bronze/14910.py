numbers = list(map(int, input().split()))
check = True
# 주어지는 수열을 받아줍니다
for i in range(1, len(numbers)):
    if numbers[i] < numbers[i - 1]:
        check = False
        break
# 수열이 비내림차순인지 확인해줍니다
if check:
    print("Good")
else:
    print("Bad")
# 확인한 결과를 출력해줍니다