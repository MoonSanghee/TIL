n = int(input())
A = list(map(int, input().split()))
# 주어지는 변수들을 받아줍니다
if n % 2:
    print("Bob")
else:
    print("Alice")
    # 수열의 길이가 짝수이면 앨리스부터 점수를 받으므로 앨리스가 이길수 있고 아니라면 앨리스가 이길수 없습니다