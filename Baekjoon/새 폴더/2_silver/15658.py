n = int(input())
numbers = list(map(int, input().split()))
cnt = list(map(int, input().split()))
# 수의 개수와 수열, 각 기호의 개수를 받아줍니다.
big = -1000000000
small = 1000000000
# 최대값과 최소값을 나올수 있는 가장 작은 수와 가장 큰 수로 설정해줍니다.
def dfs(idx, ans):
    # 수열의 위치와 현재 값을 받아줍니다.
    global big, small
    
    if idx == n:
        big = max(big, ans)
        small = min(small, ans)
        return
    # 수열의 마지막 자리까지 계산을 완료하였다면 최대값, 최소값과 비교하여 갱신해줍니다
    if cnt[0] > 0:
        cnt[0] -= 1
        dfs(idx+1, ans + numbers[idx])
        cnt[0] += 1
    if cnt[1] > 0:
        cnt[1] -= 1
        dfs(idx+1, ans - numbers[idx])
        cnt[1] += 1
    if cnt[2] > 0:
        cnt[2] -= 1
        dfs(idx+1, ans * numbers[idx])
        cnt[2] += 1
    if cnt[3] > 0:
        cnt[3] -= 1
        dfs(idx+1, int(ans / numbers[idx]))
        cnt[3] += 1
    # 각 기호가 남았는지 확인하고 남아있다면 해당 기호로 연산을 실행 후 재귀를 통해 함수를 재가동시켜줍니다.
        
dfs(1, numbers[0])
# 리스트의 첫 값과 1번 인덱스 값을 넣어 함수를 실행시킵니다.
print(big)
print(small)
# 최대값과 최소값을 차례대로 출력해줍니다.