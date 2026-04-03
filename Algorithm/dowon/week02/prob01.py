import sys
input = sys.stdin.readline

ans=0
s=set()
n, m=map(int, input().split())
for i in range(n):
    s.add(input().strip())
for i in range(m):
    if input().strip() in s:
        ans+=1
print(ans)
