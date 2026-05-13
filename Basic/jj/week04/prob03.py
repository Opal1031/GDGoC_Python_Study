def solution(citations):
    citations.sort(reverse=True)
    answer = 0
    
#     for i in range(len(citations)):
#         papers=i+1
#         cited=citations[i]
        
#         h=min(papers,cited)
#         answer=max(answer,h)
        
    for i,citation in enumerate(citations):
        
        h=min(i+1, citation)
        answer=max(answer,h)
        
            
    return answer