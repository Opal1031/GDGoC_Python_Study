def solution(citations):
    citations.sort(reverse=True)

    for i in range(len(citations)):
        if citations[i] <= i:
            return i

    return len(citations)

'''
코멘트:

[더 명확한 내림차순 방식]
citations.sort(reverse=True)

for i in range(len(citations)):
    h_index = i + 1

    if citations[i] < h_index:
        return h_index - 1

return len(citations)
'''