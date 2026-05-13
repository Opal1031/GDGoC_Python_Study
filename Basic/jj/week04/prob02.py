def solution(numbers):
    
    temp=list(map(str,numbers))
    temp=sorted(temp ,key=lambda x: x*3,reverse=True)
    answer=''.join(temp)
    
    return str(int(answer))