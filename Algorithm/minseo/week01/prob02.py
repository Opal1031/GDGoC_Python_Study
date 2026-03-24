# BOJ 1929: 소수 구하기

# 시간복잡도: O(N log (log N))

import sys
input = sys.stdin.readline

M, N = map(int, input().split())

is_prime = [True] * (N + 1)
is_prime[0] = is_prime[1] = False

for i in range(2, int(N ** 0.5) + 1):
	if is_prime[i]:
		for j in range(i * i, N + 1, i):
			is_prime[j] = False

for i in range(M, N + 1):
	if is_prime[i]:
		print(i)