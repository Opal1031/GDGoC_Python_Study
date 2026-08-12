# 프로그래머스 181829: 이차원 배열 대각선 순회하기

def solution(board, k):
    answer = 0

    for row, values in enumerate(board):
        for col, value in enumerate(values):
            if (row + col <= k):
                answer += value

    return answer