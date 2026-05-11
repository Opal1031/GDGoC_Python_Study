def solution(n):
    answer = [ n for n in range(1,n+1) if n % 2 != 0]
    return answer

'''
Comment:

Good!

answer을 선언하지 않고, return문에서 바로 리스트 컴프리헨션을 이용해서 홀수 리스트를 만들어 반환하는 방식도 있습니다.
'''