def solution(s):
    sutja = {
        'p': 0,
        'y': 0
    }

    for dab in s.lower():
        if dab in sutja:
            sutja[dab] += 1

    return sutja['p'] == sutja['y']