# 프로그래머스 178870: 연속된 부분 수열의 합

def solution(sequence, k):
    answer = []

    left = right = total = 0
    min_len = 1000000
    while (right < len(sequence)):
        total += sequence[right]

        while (total > k and left <= right):
            total -= sequence[left]
            left += 1

        if (total == k):
            if (right - left < min_len):
                min_len = right - left
                answer = [left, right]

        right += 1

    return answer