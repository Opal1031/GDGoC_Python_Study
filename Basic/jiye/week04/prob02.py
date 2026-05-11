def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x*10, reverse=True)
    answer = "".join(numbers)
    return str(int(answer))

'''
Comment:

[x*10 vs x*3]
x*3이 더 효율적입니다 (최대 3자리 숫자이므로).

x*10: '3' → '33333333333...' (10번), '30' → '303030...' (10번)
x*3:  '3' → '333', '30' → '303030'

[map() 사용]
list(map(str, numbers))로 간결하게 변환하는 것이 좋습니다.
'''