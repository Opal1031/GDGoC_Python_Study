def solution(numbers):
    answer = 0
    map_dict = {x: True for x in numbers}
    sol=[x for x in range(10) if x not in map_dict]
    for i in sol:
        answer+=i
    return answer

'''
Comment:

[이번 주제와의 연관성]
이번 주제인 '딕셔너리 활용'에 부합하는 풀이입니다.
딕셔너리를 통해 등장 여부를 빠르게 확인할 수 있습니다.

[비교]
- 두 풀이 모두 딕셔너리로 등장 여부를 체크하여 주제에 적합
- value를 0/1로 관리하면, 등장 횟수까지 확장 가능
'''