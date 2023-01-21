import sys
input = sys.stdin.readline
n = int(input())
tops = list(map(int,input().split()))
# 탑의 개수와 높이들을 받아줍니다.
answer= [0] * n
# 몇개의 탑과 수신이 가능한지 체크해줄 리스트를 만들어줍니다.
stack = []
# 교신 가능한 탑의 정보가 저장될 스택을 만들어 줍니다.
for i in range(len(tops)):
    while stack:
        if tops[stack[-1]]<tops[i]:
            stack.pop()
        else:
            answer[i] = stack[-1]+1
            break
        # 스택에 가장 뒤의 값과 현재 자리값을 비교하여 현재 높이가 더 크면 교신이 안 되므로
        # pop하여 제거해주고 높이가 더 작다면 탑의 인덱스 위치를 저장하고 있으므로 1을 더한값을 
        # answer의 자리에 넣어줍니다.
    stack.append(i)
    # 교신 가능한 자리를 확인하고 answer 값을 입력해주었다면 현재 위치를 stack에 넣어줍니다.
print(*answer)
# answer에 저장된 값들만을 출력해줍니다.