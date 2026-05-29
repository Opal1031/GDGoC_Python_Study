def solution(numbers):
    bict = {x: True for x in numbers}
    return sum(x for x in range(10) if x not in bict)