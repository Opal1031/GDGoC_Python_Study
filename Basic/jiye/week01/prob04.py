a=1
n=int(input())

for i in range(n):
    a = a * n
    n -= 1

print(a)