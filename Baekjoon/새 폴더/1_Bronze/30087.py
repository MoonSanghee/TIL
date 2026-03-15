d = {
    'Algorithm' : 204,
    'DataAnalysis' : 207,
    'ArtificialIntelligence' : 302,
    'CyberSecurity' : 'B101',
    'Network' : 303,
    'Startup' : 501,
    'TestStrategy' : 105,
}
# 강의와 강의실을 매칭하여 딕셔너리에 담아줍니다
N = int(input())
# 주어지는 강의의 수를 받아줍니다
for _ in range(N):
    word = input()
    print(d[word])
    # 강의에 해당한는 강의실을 출력해줍니다