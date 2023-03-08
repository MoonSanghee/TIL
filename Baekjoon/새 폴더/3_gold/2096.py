n =int(input())

maps = list(map(int, input().split()))

big = maps
small = maps
# 최대값과 최소값을 기록할 리스트를 처음 시작 줄과 같게 해줍니다.
for i in range(n - 1):
    new = list(map(int, input().split()))
    # 다음 줄의 값을 입력받고
    big = [max(big[0], big[1]) + new[0], max(big) + new[1], max(big[1], big[2]) +new[2]]
    # big의 0번 인덱스 값에는 0번 인덱스와 1번 인덱스의 값중 큰 값과 new의 0번 인덱스
    # 값의 합으로 1번 인덱스에는 0, 1, 2 번 인덱스 값중 가장 큰 값과 new의 1번
    # 인덱스 값의 합으로 2번 인덱스에는 1, 2번 인덱스 값중 큰 값과 new의 2번 인덱스 
    # 값의 합으로 갱신하여줍니다.
    
    small = [min(small[0], small[1]) + new[0], min(small) + new[1], min(small[1], small[2]) +new[2]]
    # 위와 같이 작은값의 합으로 값을 small의 값을 갱신하여줍니다.
 
print(max(big), min(small))
# big과 small에 마지막 줄에 도달하는 가장 큰 값이 되는 경우들과 가장 작은 경우들이
# 저장되어있으니 big에서 가장 큰 값과 small에서 가장 작은 값을 출력해줍니다.