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
