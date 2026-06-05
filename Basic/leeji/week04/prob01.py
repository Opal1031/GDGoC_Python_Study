def solution(array, commands):
    answer = []
    for i, j, k in commands:
        answer.append(sorted(array[i-1:j])[k-1])
    return answer

'''
Comment:

Good!
슬라이싱과 정렬, 인덱싱을 한 줄로 깔끔하게 처리하였습니다.
'''