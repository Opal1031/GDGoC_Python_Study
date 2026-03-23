# BOJ 2869: 달팽이는 올라가고 싶다

# 시간복잡도: O(1)

import sys
input = sys.stdin.readline

A, B, V = map(int, input().split())

print((V - B - 1) // (A - B) + 1)