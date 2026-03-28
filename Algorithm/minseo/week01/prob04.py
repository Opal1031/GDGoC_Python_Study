# BOJ 1699: 제곱수의 합

# 시간복잡도: O(N * sqrt(N))

import sys
input = sys.stdin.readline

Num = int(input())
dp = list(range(Num + 1))

for i in range(2, Num + 1):
    for j in range(1, i + 1):
        square = j * j

        if (square > i):
            break

        dp[i] = min(dp[i], dp[i - square] + 1)

print(dp[Num])