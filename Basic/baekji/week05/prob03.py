def solution(s):
    answer = True
    count_p = 0
    count_y = 0
    
    for ch in s:
        if ch == 'p' or ch == 'P':
            count_p = count_p + 1
        elif ch == 'y' or ch == 'Y':
            count_y = count_y + 1
    
    if count_p != count_y:
        answer = False
    
    return answer

'''
Comment:

[이번 주제와의 연관성]
이번 주제는 '딕셔너리 활용'입니다.
현재 풀이는 카운터 변수로 정확히 해결했으며, 딕셔너리 없이도 충분히 좋은 방식입니다.

[비교]
- minseo 풀이처럼 counts 딕셔너리를 쓰면 문자 개수 확장에 유리합니다.
- 현재 방식은 p/y 두 문자만 다뤄서 직관적이고 성능도 충분합니다.
'''
