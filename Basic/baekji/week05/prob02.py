def solution(num):
    answer = ''
    
    if num % 2 == 0:
        answer = "Even"
    else:
        answer = "Odd"
    
    return answer

'''
Comment:

[이번 주제와의 연관성]
이번 주제는 '딕셔너리 활용'입니다.
본 풀이는 if-else로 명확하게 해결했지만, 딕셔너리를 사용하진 않았습니다.

[예시 방향(딕셔너리 활용)]
- parity = {0: "Even", 1: "Odd"} 형태로 나머지 값을 매핑하면 딕셔너리 활용이 드러납니다.
- 현재 풀이도 가독성이 좋아 기본 풀이로는 충분히 좋습니다.
'''
