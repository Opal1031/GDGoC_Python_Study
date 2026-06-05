def solution(numbers):
    str_numbers = list(map(str, numbers))

    str_numbers.sort(key=lambda x: x * 3, reverse=True)

    answer = "".join(str_numbers)

    if answer[0] == "0":
        return "0"

    return answer

'''
Comment:

Good!
x * 3 정렬 방식을 잘 활용하였습니다.
모든 값이 0일 때 "0"으로 처리한 부분도 좋습니다.
'''