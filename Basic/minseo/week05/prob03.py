# 프로그래머스 12916: 문자열 내 p와 y의 개수

def solution(s):
    counts = {}

    for ch in s.lower():
        counts[ch] = counts.get(ch, 0) + 1
        
    return counts.get('p', 0) == counts.get('y', 0)