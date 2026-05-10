def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x*3, reverse = True)
    # 저 솔직히 lamda로 규칙 만들 수 있다까지는 이해했는데 왜 위에 처럼 규칙을 만들어야하는지는 이해가 안됬어요...ㅜㅜ
    answer = ''.join(numbers)
    return answer