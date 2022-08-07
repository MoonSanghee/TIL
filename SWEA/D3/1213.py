import sys

sys.stdin = open("1213_input.txt", "r")

# test_case = 10

# for test in range(1, test_case + 1):
    
#     test_num = input()
#     check_word = input()
#     sentence = input()

#     count = sentence.count(check_word)
#     print(f'#{test_num} {count}')

for _ in range(10) :
    T = int(input())
    string = input()
    sentence = input()

    count = sentence.count(string)
    print("#{} {}".format(T, count))

