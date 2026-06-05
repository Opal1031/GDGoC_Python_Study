# 프로그래머스 42839: 소수 만들기

# 시간복잡도: O(M log log M) (에라토스테네스 체), M = 생성 가능한 최대 수

from itertools import permutations

def solution(numbers):
    nums = set()

    for l in range(1, len(numbers) + 1):
        for p in permutations(numbers, l):
            nums.add(int(''.join(p)))

    if not nums:
        return 0

    max_n = max(nums)

    if (max_n < 2):
        return 0

    sieve = [True] * (max_n + 1)
    sieve[0] = sieve[1] = False

    for i in range(2, int(max_n ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, max_n + 1, i):
                sieve[j] = False

    return sum(1 for v in nums if v >= 2 and sieve[v])