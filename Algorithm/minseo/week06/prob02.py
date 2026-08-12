# 프로그래머스 12914: 멀리 뛰기

# 시간복잡도: O(N)
# 공간복잡도: O(N)

def solution(n):
    if (n <= 2):
        return n

    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 2

    for i in range(3, n + 1):
        dp[i] = (dp[i - 1] + dp[i - 2]) % 1234567

    return dp[n]