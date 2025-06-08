n, k = map(int, input().split())
arr = list(map(int, input().split()))
cnt = 0
# 주어지는 수열의 길이와 찾고자하는 교환이 몇번째인지 받고 수열을 받아줍니다
# 교환의 횟수를 담을 변수를 설정해줍니다
for i in range(n - 1, 0, -1):
    for j in range(i):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
            if cnt == k:
                result = arr[j], arr[j + 1]
        # 주어진 의사코드대로 버블정렬을 실행하면서 교환이 이루어지면 횟수를 갱신해주고 k번째 교환이 일어나면 결과에 값을 담아줍니다
if cnt < k:
    print(-1)
else:
    print(*result)
# 교환이 충분히 일어났다면 담아둔 답을 출력하고 부족하다면 -1을 출력해줍니다