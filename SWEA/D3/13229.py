T = int(input())
d = {
    "MON" : 6, 
    "TUE" : 5, 
    "WED" : 4, 
    "THU" : 3, 
    "FRI" : 2, 
    "SAT" : 1, 
    "SUN" : 7, 
}
# 테스트 케이스의 개수를 받아줍니다
# 각 요일부터 다음 일요일까지 남은 날을 딕셔너리에 담아줍니다
for t in range(T):
    word = input()
    print(f'#{t + 1} {d[word]}')
    # 주어지는 요일을 받고 결과를 주어진 양식에 맞게 출력해줍니다