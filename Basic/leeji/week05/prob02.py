def solution(num):
    cict = {
        0: "Even",
        1: "Odd"
    }

    return cict[num % 2]

'''
Comment:

[이번 주제와의 연관성]
이번 주제는 '딕셔너리 활용'입니다.
나머지 값을 딕셔너리 key로 바로 연결해서 결과를 반환하는 방식이 아주 적절합니다.
'''