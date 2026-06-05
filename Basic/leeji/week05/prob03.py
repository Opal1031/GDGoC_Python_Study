def solution(s):
    sutja = {
        'p': 0,
        'y': 0
    }

    for dab in s.lower():
        if dab in sutja:
            sutja[dab] += 1

    return sutja['p'] == sutja['y']

'''
Comment:

[이번 주제와의 연관성]
이번 주제인 '딕셔너리 활용'에 잘 맞는 풀이입니다.
문자별 등장 횟수를 딕셔너리에 누적한 뒤 p와 y를 비교하는 방식이 깔끔합니다.
'''