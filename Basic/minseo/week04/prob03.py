# 프로그래머스 42747: H-Index

def solution(citations):
    answer = 0

    citations.sort(reverse = True)

    for i, citation in enumerate(citations):
        if (i + 1 > citation):
            break
        
        answer = i + 1
    
    return answer