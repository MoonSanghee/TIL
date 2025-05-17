n = int(input())
weights = list(map(int, input().split()))
want = int(input())
numbers = list(map(int, input().split()))
# 추의 개수와 주어지는 추들, 만들고자 하는 무게의 개수와 무게들을 받아줍니다
s = set()
s.add(0)
# 추를 조합하여 만들수있는 결과를 담을 세트를 만들고 0을 넣어줍니다
for w in weights:
    new = set()
    for d in s:
        new.add(d + w)
        new.add(d - w)
    s = s.union(new)
# 모든 추를 차례대로 순회하며 만들어진 결과에서 왼쪽 혹은 오른쪽에 추를 놓았을때 결과를 새로 나오는 결과에 넣어 나올수 있는 결과값을 추가해줍니다
for i in s:
    if i < 0:
        s.add(i * -1)
# 결과값을 순회하며 음수인 경우 반대로 위치하면 양수가 되므로 양수로 전화하여 사용해줍니다
for i in numbers:
    if i in s:
        print("Y", end = ' ')
    else:
        print("N", end = ' ')
# 찾고자하는 무게를 만든 조합에 있는지 확인하여 결과를 출력해줍니다