def solution(citations):
    answer = 0
    citations.sort(reverse=True)
    for i in range(len(citations)):
        if citations[i] >= i + 1:
            answer=i+1
        else:
            break
    return answer

'''
Comment:

[논리 개선]
현재 코드는 조건을 만족할 때만 answer를 갱신합니다.
반복을 계속하면서 answer 값이 갱신되는 마지막 i 값이 h-index가 됩니다.

더 직관적으로:
  for i in range(len(citations)):
      h_index = i + 1

      if citations[i] < h_index:
          break
          
      answer = h_index

또는 다음과 같이 단순화 가능합니다:
  for i in range(len(citations)):
      if citations[i] >= i + 1:
          answer = i + 1

      else:
          break
'''