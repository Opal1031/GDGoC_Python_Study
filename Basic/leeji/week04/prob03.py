def solution(citations):

    citations.sort(reverse=True)

    hi_index = 0

    for i, citation in enumerate(citations):

        pa_count = i + 1

        if pa_count > citation:
            break

        hi_index = pa_count

    return hi_index