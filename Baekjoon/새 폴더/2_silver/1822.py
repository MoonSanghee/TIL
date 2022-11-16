a, b = map(int, input().split())
al = list(map(int, input().split()))
bl = list(map(int, input().split()))
aset = set(al)
bset = set(bl)
result = aset - bset
li = list(result)
li.sort()
print(len(li))
if len(li):
    print(*li)
# 주어진 두 리스트를 세트 형태로 변환하여 첫번째 리스트에서 두 번째 리스트를 빼주면 차집합 세트를 구하였습니다.
# 이를 다시 리스트로 변환 시키고 정렬한 다음 길이가 0 이상이라면 길이와 값들을 아니면 0이라는 길이만 출력해주었습니다.