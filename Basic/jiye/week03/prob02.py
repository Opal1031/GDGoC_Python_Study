def solution(n):
    answer = [ n for n in range(1,n+1) if n % 2 != 0]
    return answer

'''
Good!

return에서 answer로 바로 반환해도 됩니다.
'''