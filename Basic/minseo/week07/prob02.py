# 프로그래머스 181855: 문자열 묶기

def solution(strArr):
    counts = {}

    for string in strArr:
        length = len(string)
        counts[length] = counts.get(length, 0) + 1

    return max(counts.values())