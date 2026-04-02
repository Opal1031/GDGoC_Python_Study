import sys
input=sys.stdin.readline

n=int(input())

for i in range(1,n+1):
    for j in range(i):
        print("*",end="")

    print()

'''
Comment:

현재 코드에서 마지막 줄에 print()가 있습니다.
불필요한 코드이므로 제거하는 것이 좋습니다.
'''
