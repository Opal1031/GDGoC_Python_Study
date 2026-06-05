def solution(numbers):
    bict = {x: True for x in numbers}
    return sum(x for x in range(10) if x not in bict)

'''
Comment:

[이번 주제와의 연관성]
이번 주제인 '딕셔너리 활용'에 잘 맞는 풀이입니다.
딕셔너리를 통해 등장한 숫자를 빠르게 체크하고, 없는 숫자만 골라 합산하고 있습니다.
'''