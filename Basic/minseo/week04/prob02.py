# 프로그래머스 42746: 가장 큰 수

def solution(numbers):
    str_numbers = list(map(str, numbers))
    
    str_numbers.sort(key = lambda x: x * 3, reverse = True)
    
    answer = "".join(str_numbers)
    
    return str(int(answer)) if answer != "0" * len(answer) else "0"