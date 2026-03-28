import sys
input = sys.stdin.readline

n= int(input())
a=1

for i in range(1,n+1):
    a=a*i

print(a)

'''
Comment:

n이 0일 경우 1을 출력하는 조건을 추가하는 것이 좋습니다.
'''