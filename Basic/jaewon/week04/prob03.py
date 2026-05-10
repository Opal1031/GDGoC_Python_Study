def solution(citations):
    
    citations.sort(reverse = True)
                   
    answer = 0
    
    for i in range(len(citations)):
        pp_count = i + 1
        citation = citation[i]
        
        if citation >= pp_count:
            ansewr = pp_count
        else:
            break
            
    return answer