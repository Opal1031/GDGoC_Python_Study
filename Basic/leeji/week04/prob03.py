def solution(citations):

    citations.sort(reverse=True)

    hi_index = 0

    for i, citation in enumerate(citations):

        pa_count = i + 1

        if pa_count > citation:
            break

        hi_index = pa_count

    return hi_index

'''
Comment:

Good!
내림차순 정렬 후 하나씩 비교하면서 H-Index를 구하는 흐름이 자연스럽습니다.
'''