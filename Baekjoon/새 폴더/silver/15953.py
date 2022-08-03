test_case = int(input())

for test in range(test_case):
    first, second = map(int, input().split())

    first_price = [5000000] * 1 + [3000000] * 2 + [2000000] * 3 + [500000] * 4 + [300000] * 5 + [100000] * 6 + [0] *80
    second_price = []
    for i in range(5):
        second_price += [int(5120000 * (2 ** (-1 * i)))] * (2 ** i)
    
    second_price += [0] *40
    print(first_price[first - 1] + second_price[second - 1])

