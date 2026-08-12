# 프로그래머스 12945: 피보나치 수

# 시간복잡도: O(N)
# 공간복잡도: O(1)

def solution(n):
    prev2, prev1 = 0, 1

    for _ in range(2, n + 1):
        current = (prev2 + prev1) % 1234567
        prev2 = prev1
        prev1 = current

    return prev1