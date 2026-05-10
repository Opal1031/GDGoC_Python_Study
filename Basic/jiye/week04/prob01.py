def solution(array, commands):
    answer = []
    for command in commands:
        cut_first = command[0]
        cut_last = command[1]
        num = command[2]
        s_array = array[cut_first-1:cut_last]
        s_array.sort()
        answer.append(s_array[num-1])
    return answer