import sys
input = sys.stdin.readline

A, B, V=map(int, input().split())

i=(V-B)//(A-B)

if (V-B)%(A-B)!=0:
    i+=1

print(i)

'''
Comment:

sys 모듈을 사용하면 input()보다 빠르게 입력을 받을 수 있습니다.
'''