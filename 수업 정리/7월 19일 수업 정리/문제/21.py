# Q. 주어진 숫자를 뒤집은 결과를 출력하시오. 
# * 문자열이 아닌 숫자로 활용해서 풀어주세요. str() 사용 금지

# A.
number = int(input())
number_p = []
while number // 10 != 0 :
    number_p.append(number % 10)
    number //= 10
number_p.append(number)
new_number = 0
for i in range(len(number_p)):
    new_number += (10**i)*number_p[len(number_p) - i - 1]
print(new_number)
