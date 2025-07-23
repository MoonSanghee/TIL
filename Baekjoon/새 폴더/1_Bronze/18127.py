A, B = map(int, input().split())
outside = 1
result = 1
# 주어지는 물질의 크기와 온도를 받고 커지는 크기와 전체 크기를 담을 변수를 설정해줍니다
for i in range(B):
    outside += A - 2
    result += outside
# 커지는 크기를 더하고 전체 면적을 갱신해줍니다
print(result)
# 결과를 출력해줍니다