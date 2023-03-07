n, m = map(int, input().split())
passwords = dict()

for _ in range(n):
    site, password = input().split()
    passwords[site] = password
    # 메모해둔 수만큼 사이트 주소와 비밀번호를 key: value로 묶어 딕셔너리에 넣어주고

for _ in range(m):
    want = input()
    print(passwords[want])
    # 원하는 사이트의 비밀번호를 딕셔너리에서 찾아 출력해줍니다.