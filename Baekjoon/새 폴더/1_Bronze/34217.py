a, b = map(int, input().split())
c, d = map(int, input().split())
# 주어지는 역까지 걸리는 시간들과 역에서 목적기까지 걸리는 시간들을 받아줍니다
if a + c < b + d:
    print("Hanyang Univ.")
elif a + c > b + d:
    print("Yongdap")
else:
    print("Either")
# 경로의 시간을 확인해 결과를 출력해줍니다