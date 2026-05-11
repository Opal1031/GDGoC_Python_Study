def solution(citations):
    citations.sort(reverse=True)
    
    h_index = 0
    for i, citation in enumerate(citations):
        if citation >= i + 1:
            h_index = i + 1
        else:
            break
    
    return h_index

'''
Comment:

조건식을 pp_count > citation으로 작성하면 else문을 생략 가능합니다.
'''