def solution(numbers):
    list = []
    for i in numbers:
        list.append(str(i))
    list.sort(key=lambda x: x*3, reverse=True)    
    answer = ''
    for j in list:
        answer = answer + j
    if answer[0] == '0':
        return '0'
    return answer

'''
Comment:

[변수명 주의]
built-in 타입명 `list`를 변수명으로 사용하면 기본 list() 함수가 가려집니다. 
대신 `str_numbers`나 `digits` 같은 명확한 이름을 사용하세요.

[map() 사용]
변수 생성을 더 간결하게:
  str_numbers = list(map(str, numbers))

[문자열 연결 최적화]
  answer = answer + j  →  answer = ''.join(str_numbers)
  join()은 반복 문자열 연결보다 훨씬 효율적입니다.

[0 처리 개선]
현재 코드는 answer[0]을 확인하지만, 
더 명확하게 answer가 '0'만으로 이루어졌는지 확인하는 것이 좋습니다:
  return answer if answer[0] != '0' else '0'

또는:
  return str(int(answer)) if int(answer) != 0 else '0'
'''