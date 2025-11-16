bs, bc, bo, bn = map(int, input().split())
# 주어지는 변수들을 받아줍니다
bs += bn
bc += bo * 2
# s와 n은 공유할수있고 c 두 개로 o를 만들수 있으니 o에 2를 곱한값을 bc에 더해줍니다
result = min(bs // 3, bc // 6)
print(result)
# s와 c가 필요한 개수로 나눈 몫이 작을것을 출력해줍니다