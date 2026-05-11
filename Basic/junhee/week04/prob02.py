def solution(numbers):
    numbers=list(map(str,numbers))

    numbers.sort(key=lambda x:x*3,reverse=True)
    return str(int(''.join(numbers)))

'''
코멘트:

[0 처리]
만약 모든 숫자가 '0'이라면, 결과는 '0'이 되어야 합니다.
따라서, 최종적으로 만들어진 문자열이 '0'으로만 이루어져 있다면, '0'을 반환하도록 처리하는 것이 필요합니다.
'''