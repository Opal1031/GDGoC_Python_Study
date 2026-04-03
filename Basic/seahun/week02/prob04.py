import sys

num = int(sys.stdin.readline())

for i in range(1,num+1):
    print(i*"*")
    i += 1

'''
Comment:

for문을 통해 i의 값은 자동으로 증가하기 때문에 i += 1은 필요하지 않습니다.
'''