def solution(sequence, k):
    answer=[]
    b=0
    Sum=0
    length=1000000000
    for a in range(len(sequence)):
        Sum+=sequence[a]
        
        while Sum>k:
            Sum-=sequence[b]
            b+=1
        if Sum==k:
            l=a-b
            if l < length:
                length=l
                answer=[b,a]
    return answer

'''
Comment:

Good!

투 포인터(슬라이딩 윈도우)로 깔끔하게 해결했습니다.
다만 변수명 `Sum`은 내장 함수 `sum`과 혼동될 수 있어 `total` 같은 이름을 쓰면 더 좋습니다.
'''