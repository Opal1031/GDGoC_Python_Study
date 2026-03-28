# BOJ 14425: 문자열 집합

# 시간복잡도: O(N + M)

import sys
input = sys.stdin.readline

N, M = map(int, input().split())

words = {}

for _ in range(N):
    word = input().strip()
    words[word] = True

count = 0

for _ in range(M):
    if input().strip() in words:
        count += 1
        
print(count)
