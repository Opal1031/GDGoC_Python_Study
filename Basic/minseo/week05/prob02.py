# 프로그래머스 12937: 짝수와 홀수

def solution(num):
    parity = {0: 'Even', 1: 'Odd'}
    
    return parity[num % 2]