def solution(numbers):
    
    temp=list(map(str,numbers))
    temp=sorted(temp ,key=lambda x: x*3,reverse=True)
    answer=''.join(temp)
    
    return str(int(answer))

'''
Comment:

Good!
x*3을 이용하는 로직을 잘 이해하고 있는지 돌아보면 좋을 것 같습니다.
'''