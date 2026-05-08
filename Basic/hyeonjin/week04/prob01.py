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
