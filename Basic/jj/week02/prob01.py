import sys
t=int(input())
input=sys.stdin.readline

for _ in range(t):
    a,b=map(int, input().strip().split())
    print(a+b)

'''
Comment:

input을 먼저 선언하고 사용해야 sys 모듈이 적용됩니다.
'''