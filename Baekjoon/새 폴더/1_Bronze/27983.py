n = int(input())
# 주어지는 리본의 개수를 받아줍니다
X = list(map(int, input().split()))
L = list(map(int, input().split()))
C = list(input().split())
flag = False
# 리본의 위치와 길이 색을 받고 매듭을 만들수 있는지 담을 변수를 설정해줍니다
for i in range(n):
    if flag:
        break
    for j in range(i + 1, n):
        if C[i] != C[j]:
            if abs(X[i] - X[j]) <= L[i] + L[j]:
                print("YES")
                print(i + 1, j + 1)
                flag = True
                break
        # 두 리본의 색이 다르면 매듭을 지을수있는지 확인하고 매듭을 지을수 있다면 두 매듭의 번호를 출력해줍니다
else:
    print("NO")
    # 반복이 멈추지 않고 끝까지 시행되었다면 매듭을 지을 수 없습니다