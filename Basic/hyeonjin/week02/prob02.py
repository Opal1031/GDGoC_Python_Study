# BOJ 1330: 두 수 비교하기

import sys
input = sys.stdin.readline

A, B = map(int, input().split())

if (A > B):
    print(">")

elif (A < B):
    print("<")
    
else:
    print("==")