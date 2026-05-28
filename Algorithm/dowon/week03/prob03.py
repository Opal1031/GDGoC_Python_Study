def solution(s):
    answer=[]
    last={}
    for i in range(len(s)):
        c=s[i]
        if c not in  last:
            answer.append(-1)
        else:
            answer.append(i-last[c])
        last[c]=i
    return answer
