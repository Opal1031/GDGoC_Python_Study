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

'''
Comment:

[변수명 명확성]
변수명 cut_first, cut_last, num이 명확해서 좋습니다.
하지만 언패킹을 사용하면 더 간결합니다:
  for i, j, k in commands:
      sliced = array[i-1:j]
      sliced.sort()
      answer.append(sliced[k-1])

[리스트 컴프리헨션으로 간결화]
한줄로 작성 가능합니다:
  return [sorted(array[i-1:j])[k-1] for i, j, k in commands]
'''
