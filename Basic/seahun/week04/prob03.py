def solution(citations):
    citations = sorted(citations)
    l = len(citations)
    for i in range(l):
        if citations[i] >= l-i:
            return l-i
    return 0

'''
Comment:

[다른 접근: 오름차순 정렬]
다른 사람들은 내림차순 정렬을 사용했으나, seahun은 오름차순 정렬을 사용합니다.
둘 다 올바르게 동작하지만, 오름차순 접근이 더 직관적입니다.
'''