def solution(n):
    answer = []
    
    for i in range(1,n+1) :
        # if i % 2 =! 0 :
        #     return answer

        if i % 2 == 1 :
            answer.append(i)

    return answer

'''
Comment:

잘못된 부분을 주석처리하고, 예시 코드로 수정해두었습니다.

1. 같지 않다는 연산자는 !=입니다. =!는 문법적으로 틀린 표현입니다.

2. 리스트 컴프리헨션을 활용하면 아래와 같은 형태로 더 간결하게 표현할 수 있습니다.
def solution(n):
    return [i for i in range(1, n + 1) if i % 2 == 1]
'''