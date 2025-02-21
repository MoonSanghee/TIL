n=int(input())
numbers=list(map(int,input().split()))
odd=0
even=0
for i in numbers:
    if i%2==1:odd+=1
    else:even+=1
if n%2==1:odd-=1
if odd==even:print(1)
else:print(0)
# 주어진 수열을 정렬하여 새로운 정렬을 만들수 있으므로 수열의 길이가 홀수라면 홀수의 개수가 짝수 +1이 되면되고
# 길이가 짝수라면 홀수와 짝수의 개수가 같다면 원하는 조건대로 수열을 만들 수 있습니다