# 프로그래머스 181922: 수열과 구간 쿼리 4

def solution(arr, queries):
    for start, end, step in queries:
        for index in range(start, end + 1):
            if (index % step == 0):
                arr[index] += 1

    return arr