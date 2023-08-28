n = int(input())
# 수의 개수를 받아줍니다.
for _ in range(n) :
  number = input()
#   수를 받아줍니다.
  reverseNumber = number[::-1]
#   뒤집은 수를 구해줍니다.
  sumValue = str(int(number) + int(reverseNumber))
#   합을 구해줍니다.
  if sumValue == sumValue[::-1] :
    print("YES")
  else :
    print("NO")
    # 합한 값의 형태를 확인하고 결과를 출력해줍니다.