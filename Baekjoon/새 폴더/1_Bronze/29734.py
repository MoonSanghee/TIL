n, m = map(int, input().split())
t, s = map(int, input().split())
# 주어지는 변수들을 받아줍니다
Zip = n + ((n - 1) // 8) * s
Dok = t + m + ((m - 1) // 8) * (2 * t + s)
# 집과 독서실에서 과제를 할 경우 걸리는 시간들을 받아줍니다
if Zip < Dok:
    print("Zip")
    print(Zip)
else:
    print("Dok")
    print(Dok)
# 시간이 더 적게 걸리는 쪽과 적게 걸리는 시간을 출력해줍니다