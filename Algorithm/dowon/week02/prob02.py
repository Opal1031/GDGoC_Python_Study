import sys
input = sys.stdin.readline

N=int(input())
s=[]
for i in range(N):
    cmd=input().split()
    if cmd[0]=="push" :
        s.append(cmd[1])
    elif cmd[0]=="pop":
        if not s:
            print(-1)
        else:
           print(s.pop())
    elif cmd[0]=="size":
        print(len(s))
    elif cmd[0]=="empty":
        if not s:
            print(1)
        else:
            print(0)
    elif cmd[0]=="top":
        if not s:
            print(-1)
        else:
            print(s[-1])

