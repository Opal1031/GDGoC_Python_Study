def solution(s):
    answer = True
    count_p = 0
    count_y = 0
    
    for ch in s:
        if ch == 'p' or ch == 'P':
            count_p = count_p + 1
        elif ch == 'y' or ch == 'Y':
            count_y = count_y + 1
    
    if count_p != count_y:
        answer = False
    
    return answer
