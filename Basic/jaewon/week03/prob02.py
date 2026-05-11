def solution(n):
    answer = [ n for n in range(1, n+1) if n % 2 == 1 ]
    return answer

'''
Comment:

Good!
answer을 따로 선언하지 않고 바로 return 해도 됩니다.

반복문을 수행하는 과정에서 모든 n에 대한 홀수 검사 방식이 아닌,
n을 2씩 증가시키면서 홀수만 리스트에 추가하는 방식으로도 풀이할 수 있습니다.

단, 해당 문제에서는 유의미한 시간 차이가 발생하지 않으므로, 현재 풀이 방식도 충분히 효율적입니다.
'''