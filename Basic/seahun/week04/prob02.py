def solution(numbers):
    str_numbers = list(map(str, numbers))
    
    str_numbers.sort(key = lambda x: x * 3, reverse = True)
    
    answer = "".join(str_numbers)
    
    return str(int(answer)) if answer != "0" * len(answer) else "0"

'''
Comment:

[0 처리]
str(int(answer))로 자동 leading zero 제거.

대안:
  return str(int(answer)) if int(answer) != 0 else "0"
'''
