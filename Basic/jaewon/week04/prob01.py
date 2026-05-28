def solution(array, commands):
    answer = [ ]
    for command in commands:
        array1 = array[command[0]-1:command[1]]
        array1.sort()
        answer.append(array1[command[2]-1])
    return answer


'''
Comment:

[색인]
짧은 코드에서는 동작하지만 command[0]처럼 반복되면 가독성 떨어지고 실수(인덱스 오프바이원 등) 발생하기 쉬움.

[언패킹]
가독성·명시성 우수. 필요한 값 수와 순서가 맞지 않으면 즉시 오류로 알려줘 안전함.
'''