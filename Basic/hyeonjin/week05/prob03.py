def solution(s):
    answer = True
    s = s.lower()
    if s.count('p')!=s.count('y'):
        answer=False
    return answer

'''
Comment:

[이번 주제와의 연관성]
이번 주제는 '딕셔너리 활용'입니다.
본 풀이는 딕셔너리를 사용하지 않고, 문자열 메서드(count)를 활용합니다.

[예시 답안(딕셔너리 활용)]
- 딕셔너리를 이용해 각 문자의 등장 횟수를 저장
- 'p'와 'y'의 개수를 딕셔너리에서 꺼내 비교
- 딕셔너리의 활용이 명확하게 드러나는 풀이
'''