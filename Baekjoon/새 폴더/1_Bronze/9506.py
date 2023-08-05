while True:
    n = int(input())
    if n == -1: 
        break
        # 입력 값이 -1이면 반복문 종료
    arr = []
    for i in range(1, n):
        if n % i == 0:
            arr.append(i)
            # 약수를 리스트에 넣어줍니다.
    if sum(arr) == n:
        print(n, " = ", " + ".join(str(i) for i in arr), sep="")
        # 리스트 안의 모든 값의 합이 n일 때 모든 합의 결과로 출력하고
    else:
        print(n, "is NOT perfect.")
        # 아니면 완벽하지 않다고 출력해줍니다.