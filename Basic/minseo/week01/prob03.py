# BOJ 1264: 모음의 개수

import sys
input = sys.stdin.readline

while True:
    S = input().rstrip()
    
    if (S == "#"):
        break
    
    count = 0
    
    for c in S:
        if c in "aeiouAEIOU":
            count += 1
            
    print(count)