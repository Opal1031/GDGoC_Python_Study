# 프로그래머스 181844: 배열의 원소 삭제하기

def solution(arr, delete_list):
    deleted = set(delete_list)

    return [number for number in arr if number not in deleted]