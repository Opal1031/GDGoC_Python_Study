import sys

number = int(sys.stdin.readline())

for _ in range(number):
    a, b = map(int, sys.stdin.readline().split())
    print(a + b)