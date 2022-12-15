import sys
input = sys.stdin.readline
n, k = map(int, input().split())
# 입력받는 국가수와 찾기 원하는 국가를 변수에 지정한다.
s = []
for i in range(n):
    s.append(list(map(int, input().split())))
    # n번 만큼 각 국가명과 성적을 리스트형식으로 받아 빈 리스트에 넣어준다, 
s.sort(key=lambda x : (-x[1], -x[2], -x[3]))
# 람다 함수를 이용하여 1번째, 2번째, 3번째 인덱스를 차례로 내림차순 정렬해줍니다.
for i in range(n):
    if s[i][0] == k:
        index = i
        # 국가번호의 index를 찾아줍니다.
for i in range(n):
    if s[index][1:] == s[i][1:]:
        print(i + 1)
        break
    # 정렬된 배열을 검사하며 국가번호 index의 금메달, 은메달, 동메달의 수와 같다면 i에 1을 더한 값을 출력해줍니다.