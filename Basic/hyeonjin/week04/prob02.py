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