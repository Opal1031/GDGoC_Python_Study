def solution(citations):
    
    citations.sort(reverse = True)
                   
    answer = 0
    
    for i in range(len(citations)):
        pp_count = i + 1
        citation = citation[i]
        
        if citation >= pp_count:
            answer = pp_count
        else:
            break
            
    return answer

'''
Comment:

조건식을 pp_count > citation으로 작성하면 else문을 생략 가능합니다.
'''