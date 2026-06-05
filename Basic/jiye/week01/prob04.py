a=1
n=int(input())

for i in range(n):
    a = a * n
    n -= 1

print(a)

'''
Comment:

n이 0일 경우 1을 출력하는 조건을 추가하는 것이 좋습니다.
'''