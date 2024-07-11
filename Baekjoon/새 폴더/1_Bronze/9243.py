n = int(input())
a = input()
b = input()
# 덮어쓸 횟수와 주어지는 두 문자열을 받아줍니다.

success = True
# 성공적으로 덮어썼는지 확인한 결과를 담을 변수를 설정해줍니다.

if n % 2:
    for i in range(len(a)):
        if a[i] == b[i]:
            success = False
            break
else:
    if a != b:
        success = False
# n이 홀수라면 a와 b의 모든 인덱스값이 달라야 성공적으로 덮어쓴것이고 
# n이 짝수라면 a와 b가 같아야 성공적으로 덮어쓴것입니다.
if success:
    print("Deletion succeeded")
else:
    print("Deletion failed")
# 결과를 출력해줍니다.