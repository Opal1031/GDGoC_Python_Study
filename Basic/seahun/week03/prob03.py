def solution(array, n):
    count = 0
    
    for num in array:
        if num == n:
            count += 1
            
    return count

'''
Comment:

count() 함수를 이용해서 리스트에서 특정 요소의 개수를 세는 방법도 있습니다.
'''