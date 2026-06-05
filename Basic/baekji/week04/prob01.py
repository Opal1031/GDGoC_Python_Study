def solution(array,commands):
    answer=[]
    for i ,j,k in commands:
        cut=array[i-1:j]
        sorted_cut=sorted(cut)
        answer.append(sorted_cut[k-1])
    return answer

'''
Comment:

Good!

슬라이싱-정렬-인덱싱 흐름을 정확히 적용했습니다.
sorted() 함수 대신 sort() 메서드를 사용해도 좋습니다.
'''