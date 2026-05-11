def solution(array, commands):
    return [sorted(array[i-1:j])[k-1] for i,j,k in commands]

'''
코멘트:

[최적 스타일]
리스트 컴프리헨션으로 간결하고 명확합니다.
한 줄로 모든 로직을 완성했습니다.

[공백 개선]
i,j,k 뒤에 공백 추가 권장:
  for i, j, k in commands
'''