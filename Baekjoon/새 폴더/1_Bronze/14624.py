N = int(input())

if N%2:
    t = N//2
    print('*'*N)
    print(' '*(N-t-1)+'*')
    for i in range(t):
        print(' '*(t-i-1) + '*' +' '*(2*i+1)+'*')
else:
    print("I LOVE CBNU")
# 주어지는 크기를 받고 홀수라면 크기에 맞게 문양을 출력하고 아니라면 문구를 출력해줍니다