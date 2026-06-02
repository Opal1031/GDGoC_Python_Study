def solution(numbers):
    str_numbers = list(map(str, numbers))
    sorted_numbers = sorted(str_numbers, key=lambda x: x*3, reverse=True)
    answer = ''.join(sorted_numbers)
    return str(int(answer))
