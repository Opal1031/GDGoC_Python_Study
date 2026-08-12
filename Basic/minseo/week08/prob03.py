# 프로그래머스 178871: 달리기 경주

# 시간복잡도: O(N + M), M = callings의 길이

def solution(players, callings):
    positions = {player: index for index, player in enumerate(players)}

    for called in callings:
        current = positions[called]
        front = players[current - 1]

        players[current - 1], players[current] = players[current], players[current - 1]
        positions[called] -= 1
        positions[front] += 1

    return players