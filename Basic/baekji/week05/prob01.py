def solution(numbers):
    answer = -1
    
    for i in range(10):
        if i not in numbers:
            if answer == -1:
                answer = 0
            answer = answer + i
    
    return answer
