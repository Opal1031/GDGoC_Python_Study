import sys
input = sys.stdin.readline

A, B, V=map(int, input().split())
i=(V-B)//(A-B)
if (V-B)%(A-B)!=0:
    i+=1
print(i)
