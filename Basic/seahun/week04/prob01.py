def solution(array, commands):
    answer = []
    for i, j, k in commands:
        answer.append(sorted(array[i-1:j])[k-1])
    return answer

'''
Comment:

[언패킹]
for i, j, k in commands로 직접 언패킹하는 것이 깔끔합니다.
'''
