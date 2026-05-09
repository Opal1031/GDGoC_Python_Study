def solution(array, commands):
    answer = [ ]
    for command in commands:
        array1 = array[command[0]-1:command[1]]
        array1.sort()
        answer.append(array1[command[2]-1])
    return answer