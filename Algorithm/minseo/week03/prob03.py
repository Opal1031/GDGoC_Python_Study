# 프로그래머스 142086: 가장 가까운 같은 글자

def solution(s):
    pos = {}
    answer = []
    
    for i, c in enumerate(s):
        if c in pos:
            answer.append(i - pos[c])
            
        else:
            answer.append(-1)
            
        pos[c] = i
        
    return answer