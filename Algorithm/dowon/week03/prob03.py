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

'''
Comment:

Good!

enumrate() 함수를 이용해서 인덱스와 문자를 동시에 가져오는 방법도 있습니다.
'''