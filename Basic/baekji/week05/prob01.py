def solution(numbers):
    answer = -1
    
    for i in range(10):
        if i not in numbers:
            if answer == -1:
                answer = 0
            answer = answer + i
    
    return answer

'''
Comment:

[이번 주제와의 연관성]
이번 주제는 '딕셔너리 활용'입니다.
본 풀이는 반복문과 조건문으로 해결되어 정답은 맞지만, 딕셔너리 활용은 드러나지 않습니다.
딕셔너리를 사용하여 숫자 존재 여부를 저장하면 더 명확하게 딕셔너리 활용이 드러납니다.
'''
