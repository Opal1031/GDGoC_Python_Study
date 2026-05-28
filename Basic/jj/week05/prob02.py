def solution(num):
    if num%2==0:
        answer = "Even"
    else:
        answer = "Odd"
    return answer

# 아니면 return "Even" if num%2==0 else "Odd"

'''
Comment:

[이번 주제와의 연관성]
이번 주제는 '딕셔너리 활용'입니다.
본 풀이는 딕셔너리를 사용하지 않고, 조건문으로만 해결합니다.

[예시 답안(딕셔너리 활용)]

- 딕셔너리를 이용해 나머지 값에 따라 바로 결과를 반환
- 딕셔너리의 활용이 명확하게 드러나는 풀이

'''