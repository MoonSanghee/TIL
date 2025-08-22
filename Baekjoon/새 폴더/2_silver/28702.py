for i in range(3, 0, -1):
    x = input()
    if x not in ["Fizz", "Buzz", "FizzBuzz"]:
        n = int(x) + i
# 연속한 세 수가 주어지므로 문자가 아닌 수가 주어지는 경우를 찾아 찾는 수를 확인해줍니다
if n % 3 == 0 and n % 5 == 0:
    print("FizzBuzz")
elif n % 3 == 0:
    print("Fizz")
elif n % 5 == 0:
    print("Buzz")
else:
    print(n)
# 찾은 수를 출력 형태를 확인해 출력해줍니다