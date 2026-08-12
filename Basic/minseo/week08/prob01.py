# 프로그래머스 1845: 폰켓몬

# 시간복잡도: O(N)

def solution(nums):
    kinds = set(nums)
    limit = len(nums) // 2

    return min(len(kinds), limit)