def solution(citations):

    citations.sort(reverse=True)
    answer = 0
    
    for i in range(len(citations)):
        if citations[i] >= i+1:
            answer = i+1
    
    return answer

'''
Comment:

Good!
내림차순 정렬 후 i+1과 비교하는 H-Index 핵심 로직을 잘 구현했습니다.
'''
