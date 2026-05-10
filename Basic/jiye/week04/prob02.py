def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x*10, reverse=True)
    answer = "".join(numbers)
    return str(int(answer))