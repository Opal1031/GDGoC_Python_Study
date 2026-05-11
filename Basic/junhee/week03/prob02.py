def solution(n):
    answer = []
    for i in range(1,n+1):
        if i%2==1:
            answer.append(i)
    return answer

'''
Comment:

Good!

리스트 컴프리헨션을 사용해서 더 간결하게 표현할 수 있습니다.
해당 주차 자료를 참고해보세요.
'''