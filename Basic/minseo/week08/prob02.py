# 프로그래머스 42576: 완주하지 못한 선수

# 시간복잡도: O(N)

def solution(participant, completion):
    counts = {}

    for name in participant:
        counts[name] = counts.get(name, 0) + 1

    for name in completion:
        counts[name] -= 1

    for name, count in counts.items():
        if (count > 0):
            return name