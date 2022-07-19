import sys

sys.stdin = open("2063_input.txt", "r")

a = int(input())
b = sorted(list(map(int, input().split())))
print(b[a//2])