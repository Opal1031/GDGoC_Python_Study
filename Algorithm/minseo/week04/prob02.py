# 프로그래머스 43238: 입국심사

def solution(n, times):
    left, right = 1, min(times) * n
    
    while (left < right):
        mid = (left + right) // 2
        
        total = sum(mid // time for time in times)
        
        if (total < n):
            left = mid + 1
            
        else:
            right = mid
    
    return left