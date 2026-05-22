def solution(numbers):
    answer = 0
    map_dict = {x: True for x in numbers}
    sol=[x for x in range(10) if x not in map_dict]
    for i in sol:
        answer+=i
    return answer