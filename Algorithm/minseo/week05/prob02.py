# 프로그래머스 43165: 타겟 넘버

# 시간복잡도: O(2^n)

def solution(numbers, target):
    cnt = 0
    n = len(numbers)

    def dfs(i, s):
        nonlocal cnt

        if (i == n):
            if (s == target):
                cnt += 1

            return
        
        dfs(i+1, s + numbers[i])
        dfs(i+1, s - numbers[i])

    dfs(0, 0)

    return cnt