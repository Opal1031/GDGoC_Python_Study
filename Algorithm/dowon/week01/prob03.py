import sys
input = sys.stdin.readline

X, Y=map(int, input().split())
Z = (Y * 100) // X

if Z>=99: 
    print(-1)
    sys.exit()

A=(Z+1)*X - 100*Y
B=(99 - Z)

if A%B==0:
    print(A//B)

else:
    print(A//B+1)

'''
Comment:

Good!
증가하는 승률을 식으로 정리해서 바로 답을 구한 접근이 이분탐색보다 효율적입니다.
'''