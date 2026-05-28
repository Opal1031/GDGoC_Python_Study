def solution(arr):
    answer = ''
    for a in arr:
        answer += a 
    return answer

'''
Comment:

Good!

for문 안에서 바로 answer에 더해주는 방식도 괜찮지만, 파이썬에서는 join() 함수를 이용해서 리스트의 요소들을 하나의 문자열로 합칠 수 있습니다.
'''