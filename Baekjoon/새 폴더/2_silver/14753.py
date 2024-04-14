n = int(input())
numbers = list(map(int, input().split()))
numbers.sort()
# 수의 개수와 수열을 받고 오름차순으로 정렬해줍니다.
coms = [numbers[0] * numbers[1], numbers[-1] * numbers[-2], numbers[0] * numbers[1] * numbers[-1], numbers[-1] * numbers[-2] * numbers[-3]]
# 수의 범위가 음수부터 시작하므로 두 수의 조합은 앞의 두 수의 곱과 마지막 두 수의 곱을 
# 세 수의 조합은 앞의 두 수와 마지막 한 수의 곱, 마지막 세 수의 곱을 리스트에 넣어줍니다.
print(max(coms))
# 곱의 조합중에 가장 큰 수를 출력하여줍니다.