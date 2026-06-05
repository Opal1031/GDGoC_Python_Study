def solution(array, commands):
    answer=[]
    for l in commands:
        i = l[0]
        j = l[1]
        k = l[2]
        a = array[i-1:j]
        a.sort()
        b=a[k-1]
        answer.append(b)
    return answer

'''
Comment:

[변수명 개선]
변수명 l, a, b는 너무 짧아서 의미를 파악하기 어렵습니다.
언패킹을 사용하면 더 명확합니다:
  for i, j, k in commands:
      sliced = array[i-1:j]
      sliced.sort()
      answer.append(sliced[k-1])

또는 한줄로 간결하게:
  return [sorted(array[i-1:j])[k-1] for i, j, k in commands]
'''
