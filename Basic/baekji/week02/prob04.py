import sys
input=sys.stdin.readline

N=int(input())

a=0
for _ in range(N):
    a+=1
    print("*"*a)

'''
Comment:

for문에서 a를 0부터 시작해서 1씩 증가시키는 방식도 좋지만,
for문에서 i를 1부터 N까지 반복하면서 print("*" * i)로 출력하는 방식이 더 간결할 수 있습니다.

for i in range(1, N + 1):
    print("*" * i)
'''