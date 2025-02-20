n = input()
s = input()
last = s[-1]
# 입력의 길이와 이름을 받아줍니다
if last in ['q', 'w', 'e', 'r', 't', 'a', 's', 'd', 'f', 'g', 'z', 'x', 'c', 'v']:print(1)
else:print(0)
# 마지막 입력이 자음이라면 이름 마지막에 받침이있고 아니면 없습니다