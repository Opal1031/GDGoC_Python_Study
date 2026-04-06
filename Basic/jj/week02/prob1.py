import sys
t=int(input())
input=sys.stdin.readline

for _ in range(t):
    a,b=map(int, input().strip().split())
    print(a+b)
