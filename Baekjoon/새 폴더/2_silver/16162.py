N, A, D = map(int, input().split())
arr = list(map(int, input().split()))
result = 0
# 주어지는 수의 개수와 시작 수 공차를 받고 참가자들의 음을 받아줍니다
# 결과를 담을 변수를 설정해줍니다 
for i in range(N):
    if arr[i] == A + D * (result):
        result += 1
# 각 참가자들을 순회하며 X단인지 확인하여 X단이 나왔다면 다음 단으로 넘어갑니다
print(result)
# 결과를 출력해줍니다