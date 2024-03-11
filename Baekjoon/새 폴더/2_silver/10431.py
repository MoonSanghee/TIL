t = int(input())
# 테스트 케이시의 수를 받아줍니다.
for _ in range(t):
    arr = list(map(int,input().split()))
    total = 0
    # 줄을 옮긴 횟수를 담을 변수를 설정해줍니다.
    for i in range(1, len(arr) - 1):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
                total += 1
                # 이웃한 학생중 앞의 학생이 키가 더 크다면 이웃한 학생을 뒤로 보내고 이동을 표시해줍니다.
    print(arr[0], total)
    # 테스트 케이스의 번호와 물러난 걸음 수를 출력해줍니다.