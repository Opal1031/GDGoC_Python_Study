def solution(numbers):
    str_numbers = list(map(str, numbers))
    sorted_numbers = sorted(str_numbers, key=lambda x: x*3, reverse=True)
    answer = ''.join(sorted_numbers)
    return str(int(answer))

'''
Comment:

Good!
x*3 정렬 아이디어를 정확히 적용해 가장 큰 수를 잘 구성했습니다.
'''
